START 100
SR 2,2
MACRO
XYZ &A
A 1,&A
AR 2,2
MEND
L 1,D1
MACRO
ABC &Z
SR 3,3
XYZ AREA
MEND
ABC VOLUME
STOP