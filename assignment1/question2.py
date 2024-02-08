salary=float(input('Enter your Salary:'))
if(salary<=10000):
    amount=salary+0.2*(salary)+0.8*(salary)
elif(salary>10000 and salary<=20000):
    amount=salary+0.25*(salary)+0.9*(salary)
else:
    amount=salary+0.3*(salary)+0.95*(salary)
print(amount)