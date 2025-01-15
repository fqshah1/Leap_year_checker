"""Conditionals Practice Scenarios
Grading System
Write a program that asks user to enter No. of Students, Name, marks obtained and return grades accordingly.
Criteria
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F"""
"""grade_A = 91
grade_B = 81
grade_C = 78
grade_D = 60
Below_60 = "FAIL"
#A = grade_A >= 90"""
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "FAIL"
def main():
    num_students = int(input("Please enter no. of Students: "))
    for i in range(num_students):
        name = input("Please enter Name of Student: ")
        marks = int(input("Please enter marks obtained by the Student: "))
        grade = calculate_grade(marks)
        print(f"Name:{name}, Marks: {marks}, grade {grade}")

if __name__ == "__main__":
    main()





"""
}
}
if (grade_A == 90): {
 print(f"Farooq got {grade_A}" + '%' + ' your Grade' + ' A')
}
else: {
    print(f"Farooq got {grade_A}" +' %' + ' your Grade' + ' A+')
}
if (grade_B >= 80): {
 print(f"Kanwal got {grade_B}" + '%' + ' your Grade' + ' B')
}
else: {
    print(f"Kanwal got {grade_B}" + '%' + ' your Grade' + ' B')
}
if (grade_C == 70): {
 print(f"Danial got {grade_C}" + '%' + ' your Grade' + ' C')
}
else: {
    print(f"Danial got {grade_C}" + '%' + ' your Grade' + ' C')
}
if (grade_D == 60): {
 print(f"Amber got {grade_D}" + '%' + ' your Grade' + ' D')
}
else: {
    print(f"Amber got {grade_D}" + '%' + ' your Grade' + ' D')
}
if (Below_60): {
 print(f"Aasia got {Below_60}" + "ED")
}
#else: {
#    print(f"Aasia got {Below_60}" + ' %' + ' you are FA
"""