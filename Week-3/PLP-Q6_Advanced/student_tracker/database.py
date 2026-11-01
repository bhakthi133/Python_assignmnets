import json
from .models import Student

def load_students(filepath: str) -> list[Student]:
    with open(filepath, "r") as f:
        data = json.load(f)
    list=[]
    for item in data:
        student = Student(
            name=item["name"],
            scores=item["scores"]
        )
        list.append(student)
    return list