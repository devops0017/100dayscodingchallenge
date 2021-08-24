from schema import Employee
import sqlite3

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create employee table
# cursor.execute("""CREATE TABLE employees (
#                   first text,
#                   last text,
#                   salary integer)""")

emp = Employee('Yogesh','Kumar',50000,cursor)
print(em)
emp.add_employee(conn)
print(emp.get_employee())