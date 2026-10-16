"""
Topic: Decorators & Context Managers 

Implement the following two Python patterns: 
(a) Decorator @log_call: prints 'Calling <name>...' before and 'Done.' after. Apply to sum_to_n(n). 
(b) Decorator @retry(times=3): re-calls function up to 3 times on Exception. Simulate random failure. 
(c) Custom context manager TempFile: creates file on __enter__, deletes on __exit__. Write and read 3 lines. 
(d) Predict the output: 
def double(func):     
    def wrapper(x):         
        return func(x) * 2     
        return wrapper 

@double 
def square(n): 
    return n * n 

print(square(3)) 
print(square(5)) 

"""
#(a) Decorator @log_call: prints 'Calling <name>...' before and 'Done.' after. Apply to sum_to_n(n). 
def log_call(func):
    def wrapper(*args,**kargs):
        print("Calling name..")
        func(*args,**kargs)
        print("Done executing")
    return wrapper

@log_call
def sum_to_n(n):
    print("calling")
    list_n=[x for x in range(0,n+1)]
    print(f"The sum of {n} is {sum(list_n)}")

sum_to_n(5)
print("=================================================================")

#(b) Decorator @retry(times=3): re-calls function up to 3 times on Exception. Simulate random failure.
import random as rand
li=["ki",9,0.8,"hi"]

def retry(times):
    def inner(func):
        def wrapper(*args,**kargs):
            try:
                func(*args,**kargs)
            except Exception as e:
                    print(f"The exception occured is {e} and so runing 3 more times")
                    try:
                        for i in range(times):
                            func(*args,**kargs)
                    except Exception as e:
                        print(e)
        return wrapper
    return inner

@retry(times=3)
def func(x):
    z=rand.choice(li)
    y=x/z
    print(f"The res is with {z} is {y}")
func(4)


#(c) Custom context manager TempFile: creates file on __enter__, deletes on __exit__. Write and read 3 lines. 
import os
class Filemanager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self,*exc):
        self.file.close()
        if(self.mode == "r"):
            os.remove("Tempfile.txt")

print("=================================================================================")
with Filemanager("Tempfile.txt","w+") as f:
    f.write("Hi!\n")
    f.write("How r u?\n")
    f.write("Where r u?")
    print("written success")

with Filemanager("Tempfile.txt","r") as f:
    for i in range(0,3):
        read=f.readline()
        print(read.strip())
exit_conf=os.path.exists("Tempfile.txt")
if(not exit_conf):
    print("Confirmed : The file deletd after read thgrough __exit__ ncontext manager")
   



