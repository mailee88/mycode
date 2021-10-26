#!/usr/bib/env python3

# Take the following list

students = [{"name": "Steve", "score": 88}, {"name": "Becky", "score": 99}, {"name": "Chad", "score": 76}]

# And print out each of the students' names, scores, and grade they would receive (90-100 A, 80-90 B, etc)
# "Steve got a(n) 88, so this student received a(n) B"

#Steve = students[0]
#print(Steve)
#Becky = students[1]
#print(Becky)
#Chad = students[2]
#print(Chad)

for student in students:
    #print(student)
    if student['score'] >= 90:
        print(f"Student: {student['name']} got an A\n")
    elif student['score'] >= 80:
        print(f"Student: {student['name']} got a B\n")
    elif student['score'] >= 70:
        print(f"Student: {student['name']} got a C\n")
    elif student['score'] >= 60:
        print(f"Student: {student['name']} got a D\n")
    else:
        print(f"Student: {student['name']} got a F\n")


