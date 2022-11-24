class Macro:
    def __init__(self, fileName):
        self.lines = []
        self.fileName = fileName
        self.KPDBSTART = 100
        with open(fileName) as file:
            for line in file:
                self.lines.append(line.rstrip().split(" "))
        File = open("elc_" + fileName, "w")
        File.close()

    def pass1(self):
        inMacro = False
        self.mnt = {}
        self.kpdtab = {}
        self.pntab = {}
        self.mdtptr = 0
        self.mdt = []
        i = 0
        currentMacro = ""
        while i < len(self.lines):
            if self.lines[i][0] == "MACRO":
                inMacro = True
                i += 1
                macroName = self.lines[i][0]
                params = self.lines[i][1].split(",")
                kpdptr = self.KPDBSTART
                earlier = len(self.kpdtab)
                self.pntab[macroName] = {}
                currentMacro = macroName
                for p in params:
                    if "=" in p:
                        self.kpdtab[self.KPDBSTART] = (p.split("=")[0], p.split("=")[1])
                        self.KPDBSTART += 1
                    self.pntab[currentMacro].update({len(self.pntab[currentMacro]) + 1: p.split("=")[0]})
                kp = len(self.kpdtab) - earlier
                self.mnt[macroName] = (len(self.pntab[currentMacro])-kp, kp, self.mdtptr, kpdptr)

            elif inMacro and self.lines[i][0] == "MEND":
                self.mdtptr += 1
                self.mdt.append("MEND")
                currentMacro = ""
                inMacro = False

            elif inMacro:
                temp = " ".join(self.lines[i])
                for ele in self.pntab[currentMacro]:
                    temp = temp.replace(self.pntab[currentMacro][ele], f"(P,{ele})")
                self.mdt.append(temp)
                self.mdtptr += 1
            i += 1
        print("\nKeyword parameter table : ")
        print(self.kpdtab)
        print("\nParameter name table : ")
        print(self.pntab)
        print("\nMacro name table : ")
        print(self.mnt)
        print("\nMacro definition table : ")
        print(self.mdt)

    def processMacro(self, macroName, params):
        aptab = []
        for p in params:
            if "=" in p:
                key = p.split("=")[0]
                val = p.split("=")[1]
                iskpvalid = False
                startkptr = self.mnt[macroName][3]
                while (startkptr in self.kpdtab.keys()):
                    if self.kpdtab[startkptr][0] == key:
                        iskpvalid = True
                        break
                    startkptr += 1
                if iskpvalid:
                    aptab.append(val)
            else:
                aptab.append(p)
        if (len(aptab) != self.mnt[macroName][0] + self.mnt[macroName][1]):
            kptr = self.mnt[macroName][3]
            size = kptr + self.mnt[macroName][1]
            while kptr < size:
                if self.kpdtab[kptr][1] == "":
                    print("Not valid macro call")
                    exit(1)
                else:
                    aptab.append(self.kpdtab[kptr][1])
                kptr += 1
        mdptr = self.mnt[macroName][2]
        with open("elc_" + self.fileName, "a") as file:
            while (self.mdt[mdptr] != "MEND"):
                l = self.mdt[mdptr]
                for j in range(len(aptab)):
                    l = l.replace(f"(P,{j+1})", aptab[j])
                inst = l.split(" ")
                if inst[0] in self.mnt.keys():
                    self.processMacro(inst[0], inst[1].rstrip().split(","))
                else:
                    file.write("+" + l + "\n")
                    file.flush()
                mdptr += 1

    def pass2(self):
        i = 0
        inMacro = False
        while i < len(self.lines):
            if self.lines[i][0] in self.mnt.keys() and not inMacro:
                self.processMacro(self.lines[i][0], self.lines[i][1].rstrip().split(","))

            elif self.lines[i][0] == "MACRO":
                inMacro = True
            elif self.lines[i][0] == "MEND":
                inMacro = False
            elif not inMacro:
                with open("elc_" + self.fileName, "a") as file:
                    file.write(" ".join(self.lines[i]) + "\n")
            i += 1

obj = Macro("prog1.asm")
obj.pass1()
obj.pass2()