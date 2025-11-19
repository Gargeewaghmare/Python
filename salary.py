salary = int(input("Enter your salary in INR:"))
if salary<=10000:
    bonus = salary*0.10
elif salary>10000 and salary<=20000:
    bonus = salary*0.20
else:
    bonus = salary*0.40
    total_salary = salary + bonus 
    print(f"salary with a bonus is :", total_salary)        