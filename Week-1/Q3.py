""""
Topic: Control Flow: if/elif, for/while Loops 

Write a Python program that uses both for and while loops: 
(a) Print the first 15 Fibonacci numbers using a while loop. Stop early if any number exceeds 1000. 
(b) Label each printed number: 'Small' (< 10), 'Medium' (10-100), or 'Large' (> 100). 
(c) Using a for loop and range(), print a multiplication table (1 to 5) for the number 7. 
(d) Predict the output: result = [] for i in range(1, 6):     if i % 2 == 0:         result.append(i * i) print(result) x = 10 while x > 0:     x -= 3 print(x) 

"""
#(a) Print the first 15 Fibonacci numbers using a while loop. Stop early if any number exceeds 1000. 
a = 0
b = 1
count = 0
while count < 15:
    if a > 1000:
        break
    print(a)
    a=b
    b = a + b
    count=count+1
    
#(b) Label each printed number: 'Small' (< 10), 'Medium' (10-100), or 'Large' (> 100). 
while(True):
    n=int(input("Enter a number"))
    if(n<10):
        print("Small")
    elif(n>=10 or n<=100):
        print("Medium")
    else:
        print("Large")

#(c) Using a for loop and range(), print a multiplication table (1 to 5) for the number 7. 
print("for loop")
for i in range(1,6):
    print("7x",i,"=",7*i)
print("While loop")
i=1
while(i<=5):
    print("7x",i,"=",7*i)
    i=i+1

"""
#(d) Predict the output: 
result = [] 
for i in range(1, 6):     
    if i % 2 == 0:         
        result.append(i * i) 
        print(result)           output==>> [4,16]
x = 10 
while x > 0:     
    x -= 3 
    print(x)                    output==>> 7,4,1

"""

