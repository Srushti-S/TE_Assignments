class Solution:
    def solve(self, start, goal):
        start_tuple = tuple([num for sublist in start for num in sublist])
        goal_tuple = tuple([num for sublist in goal for num in sublist])

        queue = [(start, start_tuple, 0)]
        visited = set(start_tuple)

        while queue:
            current, current_tuple, steps = queue.pop(0)

            if current_tuple == goal_tuple:
                return steps

            i, j = self.find_empty(current)
            moves = self.get_valid_moves(i, j)

            for move in moves:
                new_i, new_j = move
                new_node = [row.copy() for row in current]
                new_node[i][j], new_node[new_i][new_j] = new_node[new_i][new_j], new_node[i][j]
                new_tuple = tuple([num for sublist in new_node for num in sublist])

                if new_tuple not in visited:
                    queue.append((new_node, new_tuple, steps + 1))
                    visited.add(new_tuple)
                
                    print(f"Step {steps + 1}:")         # Print step-wise matrix
                    self.print_matrix(new_node)
                    print()

        return -1

    def find_empty(self, node):
        for i, row in enumerate(node):
            if 0 in row:
                return i, row.index(0)

    def get_valid_moves(self, i, j):
        moves = []

        if i > 0:
            moves.append((i - 1, j))
        if i < 2:
            moves.append((i + 1, j))
        if j > 0:
            moves.append((i, j - 1))
        if j < 2:
            moves.append((i, j + 1))

        return moves

    def print_matrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

ob = Solution()

print("Enter the start state (row-wise):")
start = [list(map(int, input().split())) for _ in range(3)]

print("Enter the goal state (row-wise):")
goal = [list(map(int, input().split())) for _ in range(3)]

steps = ob.solve(start, goal)
print("Number of steps required:", steps)
