class Employee:

    def __init__(self,first_name,last_name,salary,sql):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.sql = sql

    def add_employee(self,conn):
        with conn:
            self.sql.execute("INSERT INTO employees VALUES (:first, :last, :salary)",
                         {'first': self.first_name, 'last': self.last_name, 'salary': self.salary})

    def get_employee(c,name):
        c.execute("SELECT * FROM employees WHERE first='{}'".format(name))
        return c.fetchall()
    #
    # def get_employee(c):
    #     c.execute("SELECT * FROM employees")
    #     return c.fetchall()

    def del_employee(self):
        pass



