"""

Write a function calculate_grade(score, total=100, passing=50) that: 

(a) Calculates percentage: (score / total) * 100. 
(b) Returns a tuple (percentage, grade): 'A' >= 90, 'B' >= 75, 'C' >= 60, 'D' >= passing, 'F' below. 
(c) Raises a ValueError if score is negative or greater than total. 
(d) Write 4 test calls demonstrating each scenario. 
(e) Predict the output: 
def grade(s, t=100, p=50):     
    pct = (s/t)*100     
    return 'Pass' if pct >= p else 'Fail' 
    print(grade(45))          ==>Fail
    print(grade(60, 150))    ===>Fail
    print(grade(80, passing=90)) ===>Eroor , there is no paarmeter named as passing

"""
def calculate_grade(score,total=100,passing=50):
    if(score<0 or score>total):
        raise ValueError ("Invalid score")
    percentage=(score/total)*100
    if(percentage>=90):
        return (percentage,'A')
    elif(percentage>=75 and percentage<90):
        return (percentage,'B')
    elif(percentage>=60 and percentage<75):
        return (percentage,'C')
    elif(percentage>=passing and percentage<60):
        return (percentage,'D')
    else:
        return (percentage,'F')
 
