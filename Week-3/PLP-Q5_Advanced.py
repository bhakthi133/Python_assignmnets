"""
Topic: Comprehensions & Functional Patterns 

Given a list of at least 6 employee dicts (name, dept, salary) across 3 departments. Use ONLY functional tools: 

(a) List comprehension: names of all 'Engineering' employees. 
(b) Dict comprehension: {name: salary} for employees earning > 60000. 
(c) Set comprehension: unique departments. 
(d) functools.reduce() to calculate total payroll. sorted() with lambda to print top 3 earners. 
(e) Predict the output: from functools import reduce emps = [{'name':'A','dept':'Eng','salary':80000},{'name':'B','dept':'HR','salary':55000},{'name':'C','dept':'Eng','salary':75000}] eng = [e['name'] for e in emps if e['dept']=='Eng'] total = reduce(lambda acc,e: acc+e['salary'], emps, 0) print(eng, total) 

"""

from functools import reduce
employees = [
    {"name": "Asha", "dept": "Engineering", "salary": 80000},
    {"name": "Rahul", "dept": "HR", "salary": 55000},
    {"name": "Priya", "dept": "Engineering", "salary": 75000},
    {"name": "Kiran", "dept": "Sales", "salary": 65000},
    {"name": "Sneha", "dept": "HR", "salary": 60000},
    {"name": "Arjun", "dept": "Engineering", "salary": 90000}
]

# (a) List comprehension: names of Engineering employees
engineering_names = [
    emp["name"] for emp in employees
    if emp["dept"] == "Engineering"
]
print("Engineering employees:", engineering_names)

# (b) Dictionary comprehension: employees earning more than 60000
high_salary = {
    emp["name"]: emp["salary"] for emp in employees
    if emp["salary"] > 60000
}
print("Employees earning above 60000:", high_salary)

# (c) Set comprehension: unique departments
departments = {emp["dept"] for emp in employees}
print("Unique departments:", departments)

# (d) reduce(): calculate total payroll
total_payroll = reduce(
    lambda total, emp: total + emp["salary"],
    employees,
    0
)
print("Total payroll:", total_payroll)

# sorted() with lambda: find the top 3 earners
top_three = sorted(
    employees,
    key=lambda emp: emp["salary"],
    reverse=True
)

print("Top 3 earners:")
for emp in top_three[:3]:
    print(emp["name"], emp["salary"])
