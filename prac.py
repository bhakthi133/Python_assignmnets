#nter the age. enter text instead of a number, display an appropriate error message.
try:
    age=int(input("Enetr"))
    print(f"The age {age}")
except ValueError as e:
    print("Invalied type")

