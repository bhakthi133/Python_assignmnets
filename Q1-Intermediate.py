"""
Topic: List/Dict Comprehensions, lambda, map, filter 

Given numbers = [3, 7, 12, 19, 24, 31, 40, 47, 56, 63]. Solve using ONLY comprehensions or functional tools: 

(a) List comprehension: all odd numbers squared. 
(b) filter() with a lambda: numbers divisible by 4. 
(c) map() with a lambda: each number zero-padded to 3 digits (e.g., 7 -> '007'). 
(d) Dict comprehension: {number: 'even'/'odd'} for all numbers. 
(e) Predict the output:
 nums = [1,2,3,4,5,6] 
 odd_sq = [x**2 for x in nums if x%2 != 0] 
 div2 = list(filter(lambda x: x%2==0, nums)) 
 padded = list(map(lambda x: str(x).zfill(3), nums[:3])) 
 print(odd_sq, div2, padded) 
 
 Output :
 odd_sq=[1,9,25]
 div2=[2,4,6]
 padded=["001","002","003"]

"""

numbers=[3, 7, 12, 19, 24, 31, 40, 47, 56, 63]
odd=[i for i in numbers if i%2!=0]
print("The odd numbers:",odd)

div_4=filter(lambda x:x%4==0,numbers)
print("The div 4 numbers:",list(div_4))

num_str=list(map(str,numbers))
padded_str=list(map(lambda x:"00"+x,num_str))
padded_int=list(map(int,padded_str))
print("The padded numbers (str):",padded_str)
print("The padded numbers (int):",padded_int)

num_d={i:"even" if i%2==0 else "odd" for i in numbers}
print("The number dictionary:",num_d)
