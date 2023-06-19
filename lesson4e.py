marks = int(input('Enter Your Marks : '))
grade = ''
"""
0-29=E
30-44=D
45-59=C
60-74=B
75> =A"""

if marks>=75 :
    grade = 'A'
elif marks >= 60 and marks <75:
    grade = 'B'
elif marks >= 45 and marks <60:
    grade = 'C'
elif marks >= 30 and marks <45:
    grade = 'D'
else :
    grade = 'E'

print(grade)