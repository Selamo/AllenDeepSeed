# ===== STUDENT GRADE MANAGER =====
gradebook ={}

def add_student():
    name = input("Enter student name: ").strip()
    if name in gradebook:
        print("Student already exits.")
    else:
        gradebook[name] = []
        print(f"Added student: {name}")
#Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

#Function to determine grade
def get_letter_grade(average):
    if average>= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >=70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
#Function to display menu  
def show_menu():
    print("\n=== STUDENT GRADEBOOK MANAGER ===")
    print("1. Add Student")
    print("2. Add Grades")
    print("3. View Student Report")
    print("4. Class Statistics")
    print("5. Exit")

#Function to add a new student
def add_grade():
    name = input("Enter the name of the Student: ").strip()
    if name in gradebook:
        grades_input = input("Enter grades of the student: ")
        try:
            grades = [float(g.strip()) for g in grades_input.split(',') if g.split()]
            invalid = [g for g in grades if not (0 <= g <= 100)]
            if invalid:
                print(f"These grades are out of range: {invalid}")
                return gradebook[name].extend(grades)
            print(f"Added grades Successfully to {name}")
        except ValueError:
            print("Invalid input. YOur numbers should be separated by commas")
    else:
            print(f"Student not found")

# Function to view students report
def view_student_report():
    name = input("Enter Student name: ").strip()
    if name in gradebook:
        grades = gradebook[name]
        if grades:
            average = calculate_average(grades)
            grading = get_letter_grade(average)
            print(f"{name}'s Average: {average} (Grade: {grading})")
            print(f"Grades: {grades}")
        else:
            print(f"{name} has no grades")
    else:
        print(f"Student not found.")

#Function to display class statistics
def class_statistics():
    if not gradebook:
        print("No Students in the gradebook")
        return 
    all_averages = {}
    for student, grades in gradebook.items():
        if grades:
            all_averages[student] = calculate_average(grades)
    if not all_averages:
        print(f"No grades available to calculate statistics.")
        return
    class_avg = sum(all_averages.values()) / len(all_averages)
    highest_student = max(all_averages, key=all_averages.get)
    lowest_student = min(all_averages, key=all_averages.get)
    print(f"\nClass Average: {class_avg}")
    print(f"Highest Student: {highest_student}")
    print(f"Lowest Student: {lowest_student}")

while True:
        show_menu()
        choice = input("Choice: ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            add_grade()
        elif choice == '3':
            view_student_report()
        elif choice == '4':
            class_statistics()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid Choice")
