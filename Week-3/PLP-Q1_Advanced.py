"""

Topic: Generators & Iterators 

Implement the following generator-based solutions: 

(a) fibonacci_gen() that yields Fibonacci numbers indefinitely (no list, no recursion). 
(b) take(n, gen) returning the first n values from any generator as a list. 
(c) squares_gen(limit) yielding squares of integers up to limit. 
(d) Use both generators to print the first 10 Fibonacci numbers that are also perfect squares. 
(e) Predict the output: 
def countdown(n):     
    while n > 0:         
        yield n         
        n -= 1 
gen = countdown(5) 
print(next(gen)) #5
print(next(gen)) #4
print(list(gen)) #[3,2,1]

"""
def fibanacci_gen(n):
    a=0
    b=1
    for i in range(n):
        yield a
        temp=a
        a=b
        b=temp+b
gen=fibanacci_gen(4)
for i in fibanacci_gen(4):
    print(i)
print(list(gen))

print("=====")
def take(n,gen):
    res=[]
    for i in range(n):
        res.append(next(gen))
    print(res) 
take(4,fibanacci_gen(4))

def squares_gen(limit):
    n=0
    while(n<limit):
        yield n*n
        n=n+1
    if(n==limit):
        raise StopIteration
try:
    for i in squares_gen(6):
        print(i)
except Exception as e:
    pass

print("======")
#(d) Use both generators to print the first 10 Fibonacci numbers that are also perfect squares.
import math
def persq(a):
    if math.isqrt(a)==a**2:
        return True
    else:
        return False
    
def gen(n):
    a=0
    b=1
    for i in range(n):
        if(persq(a)):
            yield a
        temp=a
        a=b
        b=temp+b 

for i in gen(10):
    print(i)




    