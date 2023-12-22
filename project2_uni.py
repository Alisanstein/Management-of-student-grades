import csv

def add_student():
    name = input("Enter student's name: ")
    last_name = input("Enter student's last name: ")
    student_id = input("Enter student's ID: ")
    grade = input("Enter student's grade: ")

    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, last_name, student_id, grade])

    print("Student information has been added to the file.")

def remove_student(student_id):
    students = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] != student_id:
                students.append(row)

    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("Student with ID", student_id, "has been removed.")

def display_students():
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def calculate_average_grade():
    total_grade = 0
    count = 0
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total_grade += float(row[3])
            count += 1
    average_grade = total_grade / count
    print("Average grade of students:", average_grade)

def add_course():
    course_name = input("Enter course name: ")
    grades = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            grade = input("Enter grade for " + row[0] + " " + row[1] + " in " + course_name + ": ")
            row.append(grade)
            grades.append(row)

    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(grades)

    print("Grades for", course_name, "have been added.")

def rank_students():
    students = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            avg_grade = sum(int(x) for x in row[3:]) / (len(row) - 3)
            students.append((row[0], row[1], avg_grade))

    ranked_students = sorted(students, key=lambda x: x[2], reverse=True)
    for i, student in enumerate(ranked_students, start=1):
        print(i, ".", student[0], student[1], "-", student[2])

def search_student(student_id):
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == student_id:
                print("Student found:")
                print(row)
                return
        print("Student not found.")

def remove_course(course_name):
    courses = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            del row[row.index(course_name) + 3]
            courses.append(row)

    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(courses)

    print(course_name, "has been removed from the records.")

def display_sorted_students():
    students = []
    with open('students.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            students.append(row)

    sorted_students = sorted(students, key=lambda x: (x[0], x[1]))
    for student in sorted_students:
        print(student)

while True:
    print("1. Add student 2. Remove student 3. Display list of students 4. Calculate average grade 5. Add course 6. Rank students 7. Search student 8. Remove course 9. Display list of students sorted by name 0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        student_id = input("Enter student ID to remove: ")
        remove_student(student_id)
    elif choice == "3":
        display_students()
    elif choice == "4":
        calculate_average_grade()
    elif choice == "5":
        add_course()
    elif choice == "6":
        rank_students()
    elif choice == "7":
        student_id = input("Enter student ID to search: ")
        search_student(student_id)
    elif choice == "8":
        course_name = input("Enter course name to remove: ")
        remove_course(course_name)
    elif choice == "9":
        display_sorted_students()
    elif choice == "0":
        break