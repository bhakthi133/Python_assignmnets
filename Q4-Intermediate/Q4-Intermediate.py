"""

Topic: pandas: read_csv, groupby, merge + numpy basics 

You have students.csv (student_id, name, class) and scores.csv (student_id, subject, score): 

(a) Read both into DataFrames and merge on student_id. 
(b) Use groupby to find average score per subject and per student. 
(c) Add a grade column: 'A' >= 85, 'B' >= 70, 'C' >= 55, 'F' otherwise. 
(d) Use numpy: mean, standard deviation, 75th percentile of all scores. 
(e) Predict the output: import pandas as pd data = {'name':['A','B','A','B'], 'score':[80,90,70,85]} df = pd.DataFrame(data) result = df.groupby('name')['score'].mean() print(result.to_dict()) 

"""
import pandas as pd
data={"student_id":["101","101","102","102","103","103"],
      "name":["a","a","b","b","c","c"],
      "class":[7,7,9,9,10,10]}
df1=pd.DataFrame(data)
print(df1)

datas={"student_id":["101","101","102","102","103","103"],
      "subject":["Maths","science","Maths","science","Maths","science"],
      "score":[70,49,57,98,67,87]}

df2=pd.DataFrame(datas)
print(df2)

df1.to_csv("students.csv",index=False)
df2.to_csv("scores.csv",index=False)

student_data=pd.read_csv("students.csv")
score_data=pd.read_csv("scores.csv")

print(student_data)
print(score_data)

merged_data=pd.merge(student_data,score_data,on="student_id")
print(merged_data)

print(merged_data.groupby("subject")["score"].mean())