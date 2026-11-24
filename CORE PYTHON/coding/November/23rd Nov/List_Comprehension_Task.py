salaries = [18000, 22000, 25000, 30000, 35000]
sal = [i+3000 for i in salaries]
print(sal)

#[21000, 25000, 28000, 33000, 38000]

employee_ids = [101, 102, 103, 104, 105, 106, 107, 108]
emp = [i for i in employee_ids if i%2==0]
print(emp)

#[102, 104, 106, 108]

marks = [85, 42, 76, 35, 91, 28, 67]
result = ["Pass" if i>=40 else "Fail" for i in marks]
print(result)

#['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass']

prices = [1000, 2500, 5000, 7500, 10000]
discount = [i-(i*10/100) for i in prices]
print(discount)

#[900.0, 2250.0, 4500.0, 6750.0, 9000.0]

salaries = [18000, 32000, 25000, 45000, 28000, 55000, 30000]
high_sal = [i for i in salaries if i>30000]
print(high_sal)

#[32000, 45000, 55000]

employees = ["arun", "priya", "karthik", "meena", "rahul"]
uppercase = [i.upper() for i in employees]
print(uppercase)

#['ARUN', 'PRIYA', 'KARTHIK', 'MEENA', 'RAHUL']

names = ["Arun", "Priya", "Karthik", "Meena"]
username = [i.lower()+"@kgs.com" for i in names]
print(username)

#['arun@kgs.com', 'priya@kgs.com', 'karthik@kgs.com', 'meena@kgs.com']

employees = [
    ("Arun", 25000),
    ("Priya", 45000),
    ("Karthik", 28000),
    ("Meena", 55000),
    ("Rahul", 32000)
]
res = [i for i,j in employees if j>30000]
print(res)

#['Priya', 'Meena', 'Rahul']