#Write load_students(filepath) returning a list of dicts. Handle FileNotFoundError. 
#list of dicts -> DictReader
import csv
def load_students(filepath):
    try:
        list_of_students=[]
        with open(filepath,"r",newline="") as f:
            reader=csv.DictReader(f)
            for row in reader:
                list_of_students.append(row)
    except FileNotFoundError as e:
        print("PRovide the Valid csv file")
    finally:
        return list_of_students
    
#Write calculate_stats(scores) returning: total, average, highest, lowest, grade. 
def cal_grade(total):
    if(total>=90):
        return 'A'
    elif(total<90 and total>=80):
        return 'B'
    elif(total<80 and total>=75):
        return 'C'
    elif(total<75 and total>=55):
        return 'D'
    else:
        return 'F'
    
def calculate_stats(scores):
    d_stats={}
    d_stats["total"]=sum(scores)
    d_stats["average"]=sum(scores)/len(scores)
    d_stats["highest"]=max(scores)
    d_stats["lowest"]=min(scores)
    d_stats["grade"]=cal_grade(sum(scores)/len(scores))
    return d_stats

#Write display_report(students) printing a formatted table: Name, Average, Grade, Pass/Fail
def display_report(students):
    print("\nThe Student Report")
    print("------------------------------------------")
    print("| Name   | Avergae   | Grade  | Result   |")
    print("------------------------------------------")
    for i in range(len(students)):
        d=students[i]
        res="fail" if d["grade"]=="F" else "Pass"
        print(f"| {d["Name"]}    | {d["average"]}      | {d["grade"]}      | {res}      |")
        print("------------------------------------------")
        
#Write save_report(students, output_path) saving the table + class summary to .txt.
#can use write( ), writelines(line ) lines=["line1\n","line2\n",....]  ,f.write( """ """)
def class_summary(student):
    summary_d={}
    total_students = len(student)
    passed = 0
    failed = 0
    total_average = 0
    for d in student:
        total_average = total_average + d["average"]
        if d["grade"] == "F":
            failed = failed+ 1
        else:
            passed= passed + 1
    class_average = total_average / total_students
    summary_d["total_students"]=total_students
    summary_d["class_average"]=class_average
    summary_d["Passed_Students"]=passed
    summary_d["Failed_Students"]=failed
    return summary_d

def save_report(student, output_path):
    with open(output_path, "w") as f:
        f.write("The Student Report:\n")
        f.write("""
------------------------------------------
| Name   | Avergae   | Grade  | Result   |
------------------------------------------\n""")
        for i in range(len(student)):
            d=student[i]
            res="fail" if d["grade"]=="F" else "Pass"
            f.write(
f"| {d["Name"]}    | {d["average"]}      | {d["grade"]}      | {res}      |\n")
            f.write(
"------------------------------------------\n")
        summary=class_summary(student)
        f.write("\n The class Summary:")
        f.write(f"\n Total Students = {summary["total_students"]}")
        f.write(f"\n Class Average = {summary["class_average"]}")
        f.write(f"\n Number of students passed = {summary["Passed_Students"]}")
        f.write(f"\n Number of students failed = {summary["Failed_Students"]}")


def main():
    input_path = input(f"\nEnter input file path: ")
    if(input_path==""):
        input_path="students_input.csv"
    students_list=load_students(input_path)
    print("\nThe student list extracted from csv file:")
    print(students_list)

    for i in range(len(students_list)):
        d=students_list[i]
        scores=[]
        for key in d:
            if key != "Name":
                scores.append(int(d[key]))
        d_stats=(calculate_stats(scores))
        d.update(d_stats)

    display_report(students_list)

    print("\nThe Report is saved in grades_report.txt file\n")
    save_report(students_list,"grades_report.txt")

if __name__=="__main__":
    main()



    
