# ============================================
# PYTHON INTERVIEW QUESTIONS & ANSWERS
# Source-style format for GitHub repository
# 01/02/2026 - reference - W3schools
# ============================================

"""
1) What is the difference between global and local scope?

- A variable created inside a function belongs to the local scope and can only be used inside that function.
- A variable created in the main body of the Python code is a global variable and belongs to the global scope.
- Global variables are available from within any scope, global and local.
"""

# Example:
x = 10  # global

def demo():
    y = 5  # local
    print("Inside function:", x, y)

demo()
print("Outside function:", x)


"""
2) What is an iterator in Python?

- An iterator is an object that contains a countable number of values.
- It can be iterated upon using a loop.
- Technically, it must implement __iter__() and __next__().
"""

lst = [1, 2, 3]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))


"""
3) What is the __init__() function in Python?

- __init__() is a constructor method.
- It is automatically executed when an object is created.
- Used to initialize object attributes.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Ali", 25)
print(p.name, p.age)


"""
4) When should you use lambda functions in Python?

- Use lambda when you need a small, anonymous function for a short time.
"""

square = lambda x: x * x
print(square(5))


"""
5) What is the difference between lists, tuples, and sets?

- List: Ordered, changeable, allows duplicates.
- Tuple: Ordered, unchangeable, allows duplicates.
- Set: Unordered, unindexed, unique values only.
"""

lst = [1, 2, 2, 3]
tpl = (1, 2, 2, 3)
st = {1, 2, 2, 3}
print(lst, tpl, st)


"""
6) How can you check if all characters in a string are alphanumeric?

- Use isalnum() method.
"""

s = "Python123"
print(s.isalnum())


"""
7) How can you convert a string to an integer?
"""

num = "5"
convert = int(num)
print(convert)


"""
8) What is indentation in Python, and why is it important?

- Indentation refers to spaces at the beginning of a line.
- Python uses indentation to define code blocks.
- Without correct indentation, Python throws an error.
"""


"""
9) What is the correct syntax to output the type of a variable?
"""

x = 10
print(type(x))


"""
10) Which collection does not allow duplicate members?

- Set
"""

st = {1, 2, 2, 3}
print(st)

# 02/02/2026 - reference - W3schools

"""
11) What is Inheritance in Python?

- Inheritance allows a class to acquire properties and methods from another class.
- Parent class = base class
- Child class = derived class
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()


"""
12) What is the output of the following code?

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
"""

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


"""
13) List Python's primary built-in data types by category:

Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
"""


"""
14) What are Membership Operators?

- Used to test if a value is present in a sequence.
- Operators: in, not in
"""

x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)


"""
15) Which statement can be used to avoid errors if an if statement has no content?

- pass
"""

if True:
    pass


"""
16) What are Arbitrary Arguments (*args)?

- Used when you don't know how many arguments will be passed.
- *args collects arguments into a tuple.
"""

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))


"""
17) How can you create and use a Module in Python?

- Create a file with .py extension.
- Import it using import keyword.
"""

# Example (assume mymodule.py exists):
# import mymodule
# mymodule.greeting("Jonathan")


"""
18) Can you copy a list using: list2 = list1?

- No, it creates a reference.
- Use copy() or list() to make a real copy.
"""

list1 = [1, 2, 3]
list2 = list1.copy()
list1.append(4)
print(list1, list2)


"""
19) How can you return a range of characters from a string?

- Use slicing.
"""

b = "Hello, World!"
print(b[2:5])


"""
20) What is a class in Python, and how do you use it?

- A class is a blueprint for creating objects.
"""

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


# ============================================
# END OF PYTHON INTERVIEW QUESTIONS FILE
# ============================================
