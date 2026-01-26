"""
MODULE 1: PYTHON BASICS
Concepts Covered:
- What is Python & Who Invented It
- Python Syntax
- Indentation
- Variables
- Comments
- Input & Output
- Data Types
- Type Casting
- Multiple Assignment
- Variable Naming Rules
- Constants
- Practice Programs
"""

# ============================================
# 1️⃣ WHAT IS PYTHON?
# ============================================
"""
Python is a high-level, general-purpose programming language.
- Invented by: Guido van Rossum
- Year: 1991
- Why Python? 
   * Easy to learn and read
   * Clean syntax (uses indentation instead of curly braces)
   * Large community & libraries
   * Used in AI, Web Development, Data Science, Automation, etc.
"""

print("\n--- WHAT IS PYTHON? ---")
print("Python is beginner-friendly, readable, and widely used around the world.")

# ============================================
# 2️⃣ PYTHON SYNTAX
# ============================================
print("\n--- PYTHON SYNTAX ---")
print("This is a simple Python program showing basic syntax.")

# ============================================
# 3️⃣ INDENTATION
# ============================================
print("\n--- INDENTATION ---")

age = 18

if age >= 18:
    print("You are eligible to vote.")
    print("This line is inside the if block.")

print("This line is outside the if block.")

# Wrong indentation example (commented to avoid error)
# if age >= 18:
# print("This will cause IndentationError")

# ============================================
# 4️⃣ VARIABLES
# ============================================
print("\n--- VARIABLES ---")

student_name = "Sumyya"   # String
student_age = 20         # Integer
student_marks = 88.5     # Float
is_present = True        # Boolean

print(student_name)
print(student_age)
print(student_marks)
print(is_present)

# ============================================
# 5️⃣ COMMENTS
# ============================================
print("\n--- COMMENTS ---")

# This is a single-line comment

"""
This is a multi-line comment.
Used to explain sections of code or notes.
"""

print("Comments make code easier to read and understand.")

# ============================================
# 6️⃣ INPUT & OUTPUT
# ============================================
print("\n--- INPUT & OUTPUT ---")

city = input("Enter your city: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

print("You live in", city)
print("You are", age, "years old")

# ============================================
# 7️⃣ DATA TYPES
# ============================================
print("\n--- DATA TYPES ---")

roll_no = 25          # int
price = 499.99        # float
course = "Python"     # string
is_online = False     # boolean

print("Type of roll_no:", type(roll_no))
print("Type of price:", type(price))
print("Type of course:", type(course))
print("Type of is_online:", type(is_online))

# ============================================
# 8️⃣ TYPE CASTING
# ============================================
print("\n--- TYPE CASTING ---")

num1 = "15"
num2 = "5"

# Convert strings to integers to add
sum_result = int(num1) + int(num2)
print("Sum after type casting:", sum_result)

decimal_value = float("3.14")
print("Decimal value:", decimal_value)

# Convert integer to string
age_text = str(age)
print("My age is " + age_text)

# ============================================
# 9️⃣ MULTIPLE ASSIGNMENT
# ============================================
print("\n--- MULTIPLE ASSIGNMENT ---")

a, b, c = 10, 20, 30
print("a, b, c =", a, b, c)

x = y = z = 100
print("x, y, z =", x, y, z)

# ============================================
# 10️⃣ VARIABLE NAMING RULES
# ============================================
print("\n--- VARIABLE NAMING RULES ---")

valid_name = "Python"
_valid_name = "Python"
validName = "Python"
VALID_NAME = "Python"

print(valid_name)
print(_valid_name)
print(validName)
print(VALID_NAME)

# Invalid examples (won't work)
# 1name = "Error"
# my-name = "Error"
# my name = "Error"

# ============================================
# 11️⃣ CONSTANTS (BY CONVENTION)
# ============================================
print("\n--- CONSTANTS (BY CONVENTION) ---")

PI = 3.14159
MAX_USERS = 1000

print("PI:", PI)
print("MAX_USERS:", MAX_USERS)

# ============================================
# 12️⃣ PRACTICE PROGRAMS
# ============================================

# Program 1: Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Program 2: Area of rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)

# Program 3: Check even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

print("\n✅ MODULE 1 COMPLETE ✅")
