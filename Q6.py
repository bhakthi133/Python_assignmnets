"""

Topic: Exception Handling: try/except/finally 

Write two functions demonstrating proper exception handling: 
(a) safe_divide(a, b): handle ZeroDivisionError and TypeError. Show 3 test calls. 
(b) read_student_file(filename): handle FileNotFoundError, use finally to print 'File operation complete'. 
(c) Write a main block calling both functions with values that trigger each exception and values that succeed. 
(d) Predict the output: 
def safe_div(a, b):     
    try:         return a / b     
    except ZeroDivisionError:         return 'Zero!'     
    finally:         print('Done') 
    print(safe_div(10, 2))           ==>> 5 Done
    print(safe_div(5, 0))            ==>> 0 Done

"""
def safe_divide(a,b):
    try:
        res=a/b
    except ZeroDivisionError as e:
        print("Invalid denominator")
    except TypeError as e:
        print("The type error (type mismatch of input)")
    else:
        print("result:", res)

def read_student_file(filename):
    try:
        with open(filename,"r")as f:
            print(f.readlines())
    except FileNotFoundError as e:
        print("Provide the valid filename")
    else:
        print("The file content is readed")
    finally:
        print(f"The file opeartion on {filename} complete")
        print("\n")

safe_divide(6,3)
safe_divide(3,0)
safe_divide(0,"8")
print("================================================================================================================")
read_student_file("Students.txt")
read_student_file(r"C:\Users\Admin\Desktop\Practice&assignmnet foler\Assignmnet_questions_solution\Python_assignmnets\Q5\Students.txt")