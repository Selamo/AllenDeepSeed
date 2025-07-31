gradebook ={}

def student_stacts(choice, name, grade):
    print("""
    1. Add Student
    2. Add Grade
    3. View Student Report
    4. Class Statistics
    5. Exit
        """)
    
    while True:
        choice = int(input("Enter the option"))
        if choice == 5:
            break

        elif choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            view_report()
        elif choice == 4:
            view_statistics()
            
        # if name not in gradebook:
        #     if name.strip().lower() == "exit":

        #     gradebook[name] = {}
        #     print(f"Student {name} added")
        # else:
        #     print(f"Name already exist")
        # break
def add_student(student_name):
    if student_name not in gradebook:
        gradebook[student_name] = {}
        print(f"Student {student_name} added")
    else:
        print(f"Student Already exist")


def add_grade(name, subject,grade):
    # name = input(f"Enter the User name for the grade to be added")
    if name in gradebook:
        gradebook[name][subject] = grade
        print(f"The grade of {name} has been added")


def calculate_average(name):
    if name in gradebook and gradebook[name]:
       grades = int(list(gradebook[name].values()))
       average = sum(grades)/len(grades)
       return average

# add_student("Allen")
# add_grade("Allen", "Maths", "30")
# add_grade("Allen", "chem", "60")
# calculate_average("Allen")

def view_report(name):
    name = input("Enter the studentto view his/her Report")
    calculate_average(name)
    if calculate_average(name) >= 90:
        grade = "A"
    elif calculate_average(name) >= 80:
        grade = "B"
    elif calculate_average(name) >= 70:
        grade = "C"
    elif calculate_average(name) >= 60:
        grade = "D"
    else:
        grade = "F"
    print("{name} average is: {calculate_average} (Grade: {grade}") 

    pass


def view_statistics():
    pass



# student_stacts("Alice", 2)