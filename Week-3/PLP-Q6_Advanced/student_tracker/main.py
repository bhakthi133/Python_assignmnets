from . import load_students
import json

def main():
    try:
        students = load_students("student_tracker/Student.json")

        for student in students:
            print(student.name, round(student.average, 2))

    except FileNotFoundError:
        print("Error: Students file not found.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error: Invalid student data: {error}")

    except ZeroDivisionError:
        print("Error: A student has no scores.")

if __name__=="__main__":
    main()


