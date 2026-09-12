import csv
import os
FILE = "student_results.csv"

def menu():
    print("\n ------STUDENT RESULT MANAGEMENT SYSTEM------")
    print("1. Add Student Result")
    print("2. Get Student Result")
    print("3. Show All Student Result")
    print("4. Exit")

def get_marks(sub):
    while True:
        try:
            m = int(input(f"{sub}: "))
            if 0 <= m <= 100:
                return m
            else:
                print(" 0-100 madhech tak!")
        except:
            print(" Fakt number tak!")

def add_result():
    roll_num = input("Enter Roll No: ")
    name = input("Enter your name: ")
    course = input("Enter your course: ")
    print("Enter Subject Marks in between 0-100")
    m1 = get_marks("marks 1")
    m2 = get_marks("marks 2")
    m3 = get_marks("marks 3")
    m4 = get_marks("marks 4")
    m5 = get_marks("marks 5")
    marks = [m1, m2, m3, m4, m5]
    return marks, course, roll_num, name

def calculate_result(marks, course, roll_num, name):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A Pass"
    elif percentage >= 75:
        grade = "B Pass"
    elif percentage >= 60:
        grade = "C Pass"
    elif percentage >= 40:
        grade = "D Pass"
    else:
        grade = "F Fail"
    print(f"\nRoll: {roll_num} | Name: {name} | Total: {total} | {percentage}% | {grade}")
    new = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["Roll No","Name","Course","Total","Percentage","Grade"])
        w.writerow([roll_num,name,course,total,percentage,grade])

def get_result():
    roll = input("\nEnter Roll No: ")
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == roll:
                    print("\n--- Result Mil Gaya ---")
                    print(f"Roll No: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Course: {row[2]}")
                    print(f"Total: {row[3]}")
                    print(f"Percentage: {row[4]}%")
                    print(f"Grade: {row[5]}")
                    return
        print(" Invalid Roll No.")
    except FileNotFoundError:
        print(" Data do not exist")

def show_all_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            print(f"\n{'Roll No':<8} {'Name':<10} {'Course':<8} {'Total':<6} {'Per':<8} {'Grade'}")
            print("-"*60)
            for row in reader:
                print(f"{row[0]:<8} {row[1]:<10} {row[2]:<8} {row[3]:<6} {row[4]:<8} {row[5]}")
            print("-"*60)
    except FileNotFoundError:
        print(" Data do not exist")

while True:
    menu()
    ch = input("Choice tak: ")
    if ch == '1':
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"\n--- Student {i+1}/{n} ---")
            marks, course, roll_num, name = add_result()
            calculate_result(marks, course, roll_num, name)
    elif ch == '2':
        get_result()
    elif ch == '3':
        show_all_data()
    elif ch == '4':
        print("Bye!")
        break
    else:
        print("Wrong choice!")