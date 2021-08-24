from schema import Employee
import sqlite3

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create employee table

# cursor.execute("""CREATE TABLE employees (
#                   first text,
#                   last text,
#                   salary integer)""")
#

print('********* Employee Management System *************')
print('Select action\n1. Add employee\n2. Find employee')
inp = input('Enter choice: ')
if inp == 1:
    emp_first = input('Enter first name: ')
    emp_last = input('Enter Last name: ')
    emp_salary = input('Enter Salary: ')
    emp = Employee(emp_first,emp_last,emp_salary,cursor)
    emp.add_employee
elif inp == 2:
    emp = Employee(emp_first,emp_last,emp_salary,cursor)

print('\nRecord has been successfully added!!!')