
# ======================================================
# MODULE 8: OBJECT-ORIENTED PROGRAMMING (OOP)
# ======================================================
print("\n--- MODULE 8: OOP ---")

# Class & Object
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("Name:",self.name,"Roll:",self.roll)

s1=Student("Sumyya",101)
s1.display()

# Inheritance
class Person:
    def speak(self):
        print("I am a person")
class Teacher(Person):
    def teach(self):
        print("I teach students")

t=Teacher()
t.speak()
t.teach()

# Polymorphism
class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")
def make_sound(animal):
    animal.sound()
make_sound(Cat())
make_sound(Dog())

# Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("Balance:",self.__balance)

acct=BankAccount(1000)
acct.deposit(500)
acct.withdraw(300)
acct.show_balance()

print("\n✅ CORE MODULES 1 TO 7 COMPLETE ✅")
