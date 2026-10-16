User_name=input("Enter your name: ")
Age=input("Enter your age: ")
Age=int(Age)
birth_year=2026-Age
print("The birth year: ",birth_year)
if(Age%2==0):
    print("Age is even")
else:
    print("Age is odd")
print("Type of age before conversion",type(Age))
age=Age/80
age=round(age,4)
print("Type of age after conversion",type(age))

"""
Predict output:-
 x = '15' 
 y = int(x) 
 z = float(y) / 4 
 print(type(x).__name__, y * 2, round(z, 2), y % 2 == 0)
 ##O/p => str
          30
          3.75
          True or 1
"""




