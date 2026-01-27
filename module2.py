"""
MODULE 2: OPERATORS + CONTROL FLOW
Concepts Covered:
- What are Operators
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Membership Operators
- Identity Operators
- Bitwise Operators (Intro)
- Control Flow (if, elif, else)
- for loop
- while loop
- break, continue, pass
- Practice Programs
"""

# =================================================
# 1️⃣ WHAT ARE OPERATORS?
# =================================================
"""
Operators are special symbols used to perform operations on values or variables.
Example: +, -, *, /, ==, >, and, or, etc.
They help us calculate, compare, and make decisions in programs.
"""

print("\n--- WHAT ARE OPERATORS? ---")
print("Operators help us perform calculations and logic in Python.")

# =================================================
# 2️⃣ ARITHMETIC OPERATORS
# =================================================
print("\n--- ARITHMETIC OPERATORS ---")

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder (Modulus):", a % b)
print("Power:", a ** b)

# =================================================
# 3️⃣ COMPARISON OPERATORS
# =================================================
print("\n--- COMPARISON OPERATORS ---")

x = 15
y = 20

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# =================================================
# 4️⃣ LOGICAL OPERATORS
# =================================================
print("\n--- LOGICAL OPERATORS ---")

is_student = True
has_id = False

print("is_student and has_id:", is_student and has_id)
print("is_student or has_id:", is_student or has_id)
print("not is_student:", not is_student)

# =================================================
# 5️⃣ ASSIGNMENT OPERATORS
# =================================================
print("\n--- ASSIGNMENT OPERATORS ---")

score = 50
print("Initial score:", score)

score += 10
print("After += 10:", score)

score -= 5
print("After -= 5:", score)

score *= 2
print("After *= 2:", score)

score /= 5
print("After /= 5:", score)

# =================================================
# 6️⃣ MEMBERSHIP OPERATORS
# =================================================
print("\n--- MEMBERSHIP OPERATORS ---")

fruits = ["apple", "banana", "mango"]

print("'apple' in fruits:", "apple" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

# =================================================
# 7️⃣ IDENTITY OPERATORS
# =================================================
print("\n--- IDENTITY OPERATORS ---")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)
print("a == b:", a == b)
print("a is c:", a is c)
print("a is not c:", a is not c)

# =================================================
# 8️⃣ BITWISE OPERATORS (INTRO)
# =================================================
print("\n--- BITWISE OPERATORS ---")

m = 5   # 101 in binary
n = 3   # 011 in binary

print("m & n:", m & n)
print("m | n:", m | n)
print("m ^ n:", m ^ n)
print("~m:", ~m)
print("m << 1:", m << 1)
print("m >> 1:", m >> 1)

# =================================================
# 9️⃣ CONTROL FLOW (if, elif, else)
# =================================================
print("\n--- CONTROL FLOW: if, elif, else ---")

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")

# =================================================
# 🔟 for LOOP
# =================================================
print("\n--- for LOOP ---")

for i in range(1, 6):
    print("Number:", i)

# =================================================
# 1️⃣1️⃣ while LOOP
# =================================================
print("\n--- while LOOP ---")

count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1

print("Blast off!")

# =================================================
# 1️⃣2️⃣ break, continue, pass
# =================================================
print("\n--- break, continue, pass ---")

# break example
for i in range(1, 11):
    if i == 6:
        break
    print("Break example:", i)

# continue example
for i in range(1, 11):
    if i == 4:
        continue
    print("Continue example:", i)

# pass example
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print("Pass example:", i)

# =================================================
# 1️⃣3️⃣ PRACTICE PROGRAMS
# =================================================

# Program 1: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Add:", num1 + num2)
print("Subtract:", num1 - num2)
print("Multiply:", num1 * num2)
print("Divide:", num1 / num2)

# Program 2: Check number type
number = float(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Program 3: Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Program 4: Print even numbers from 1 to 20
print("\nEven numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Program 5: Password checker
correct_password = "python123"

while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")

print("\n✅ MODULE 2 COMPLETE (OPERATORS + CONTROL FLOW) ✅")
