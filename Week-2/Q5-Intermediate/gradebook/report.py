def generate_report(student):
    total=sum(student[1:])
    avg=(total/(len(student)-1))
    result="Pass" if avg>=35 else "FAil"
    print(f"{student[0]} : \n Total={total} \n Avg={avg} \n Result={result}\n")

