"""

Topic: Lists, Tuples, Sets & Dictionaries 

You are given this list of student scores: [85, 92, 78, 92, 88, 78, 95, 88, 70, 92]. Write a program that: 

(a) Removes duplicates using a set and prints the unique scores. 
(b) Builds a dictionary mapping each unique score to how many students got it. 
(c) Sorts the dictionary by score in ascending order and prints it neatly. 
(d) Uses a tuple to store and print the (min, max, count) of the original list. 
(e) Predict the output: 
nums = [4, 7, 4, 2, 7, 9] 
unique = set(nums)                                ==>unique=[4,7,2,9]
counts = {n: nums.count(n) for n in unique}       ==>counts={4:2,7:2,2:1,9:1}
print(sorted(counts.items()))                     ==>[(2, 1), (4, 2), (7, 2), (9, 1)]

"""

def remove_dup(score):
    score_set=set(score)
    for x in score_set:
        print(x)

def dict_count(score):
    d={}
    for i in score:
        d[i]=d.get(i,0)+1
    return d

def sort_dict(d,score):
    score.sort()
    d={}
    for i in score:
        d[i]=d.get(i,0)+1
    print(d)

def tup_op(score):
    t=(min(score),max(score),len(score))
    print(t)

score=[85, 92, 78, 92, 88, 78, 95, 88, 70, 92]
remove_dup(score)
d=dict_count(score)
print(d)
sort_dict(d,score)
tup_op(score)