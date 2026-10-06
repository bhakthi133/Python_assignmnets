"""
Topic: String Operations & File I/O 

Write a program reading students.txt (format: 'Name,Score' per line): 
(a) Read and print each student's name in UPPER CASE followed by their score. 
(b) Calculate and print the class average. 
(c) Identify and print the student with the highest score. 
(d) Append a summary line: 'Class Average: XX.X | Total Students: N'. Use at least 3 string methods. 
(e) Predict the output: 
data = 'Alice,85\nBob,92\nCarol,78' 
lines = data.strip().split('\n') 
scores = [int(l.split(',')[1]) for l in lines] 
print(max(scores) 
round(sum(scores)/len(scores), 1))  ==>> gives the average of the scores of all students and rounds it to one decimal

"""
with open ("Students.txt","r") as f:
    sum=0
    lines=f.readlines()
    d={}
    for line in lines:
        name_score=[]
        name_score=line.strip().split(",")
        d[name_score[0]]=int(name_score[1])

    #a
    for k in d:
        print(k.upper(),":",d[k])

    #b
    sum=0
    for k in d:
        sum=sum+d[k]
    avg=sum/len(d)
    print("average:",sum/len(d))

    #c
    max_score_student=[]
    val=d.values()
    max_score=max(val)
    for k in d:
        if(d[k]==max_score):
            max_score_student.append(k)
    print("The highest score students with",max_score,":",max_score_student)

    #d
    summary=f"Class average {avg:.1f} | Total Student: {len(d)}"
    with open("Students.txt","a") as f:
        writer=f.write("\n")
        writer=f.write(summary)
    
    
        
