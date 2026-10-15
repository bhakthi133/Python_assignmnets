"""

Topic: Decorators & Context Managers 

Implement the following two Python patterns: 
(a) Decorator @log_call: prints 'Calling <name>...' before and 'Done.' after. Apply to sum_to_n(n). 
(b) Decorator @retry(times=3): re-calls function up to 3 times on Exception. Simulate random failure. 
(c) Custom context manager TempFile: creates file on __enter__, deletes on __exit__. Write and read 3 lines. 
(d) Predict the output: def double(func):     def wrapper(x):         return func(x) * 2     return wrapper @double def square(n): return n * n print(square(3)) print(square(5)) 

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