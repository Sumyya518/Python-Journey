# ======================================================
# MODULE 5: FUNCTIONS
# ======================================================
print("\n--- MODULE 5: FUNCTIONS ---")

def greet():
    print("Hello! Welcome to Python.")

greet()

def greet_user(name):
    print("Hello", name)

greet_user("Sumyya")

def add(a,b):
    return a+b

print("Add:", add(10,5))

# Default param
def welcome(name="Student"):
    print("Welcome", name)
welcome()
welcome("Sumyya")

# Variable-length arguments
def total_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print("Total sum:", total_sum(1,2,3,4,5))
