#OOP Excercise1:Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle = Vehicle('bus',100,20)
print(vehicle.max_speed, vehicle.mileage)


#OOP Exercise 2: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle):

    def seating_capacity(self,capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers'

bus_model = Bus('volvo',200,20)
print(f'Bus model is {bus_model.name} and it has top speed of {bus_model.max_speed} and {bus_model.mileage} mileage')
print(bus_model.seating_capacity(30))

#OOP Exercise 3: Bank account which mantains bank balance and perform two operations i.e deposit/withdrawl

class Bankaccount:
    def __init__(self):
        self.balance = 100


    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

#Inherited bankaccount class to check for minimum balance

class MinimumBalanceAccount(Bankaccount):
    def __init__(self,minimum_balance):
        Bankaccount.__init__(self)
        self.minimum_balance = minimum_balance


    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            Bankaccount.withdraw(self,amount)


