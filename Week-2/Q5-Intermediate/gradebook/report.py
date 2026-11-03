def generate_report(student):
    total=student.m1+student.m2+student.m3
    avg=(total/3)
    result="Pass" if avg>=35 else "FAil"
    print(f"{student[0]} : \n Total={total} \n Avg={avg} \n Result={result}\n")

    marks=student.m1+student.m2+student.m3
    name=student.name