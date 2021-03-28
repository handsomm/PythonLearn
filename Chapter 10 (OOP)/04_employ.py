class Employee:
    company = "Google"
    salary = 100

shibu = Employee()
cbu = Employee()
shibu.salary = 300

print(shibu.company)
print(cbu.company)

Employee.company = "youtube"
print(shibu.company)
print(cbu.company)
print(shibu.salary)