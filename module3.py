"""
PYTHON COURSE — CORE MODULES (3 TO 8)
Covers: Strings, Lists, Tuples, Sets, Dictionaries, Functions, File Handling, OOP, Exception Handling
"""

# ======================================================
# MODULE 3: STRINGS
# ======================================================
print("\n--- MODULE 3: STRINGS ---")

text = "Python Programming"

# Indexing & Slicing
print("First character:", text[0])
print("Last character:", text[-1])
print("First 6 chars:", text[0:6])
print("From 7th char to end:", text[7:])
print("Reverse string:", text[::-1])

# String Methods
email = "User@Example.COM"
print("Lowercase:", email.lower())
print("Uppercase:", email.upper())
print("Replace Example with Mail:", email.replace("Example","Mail"))
print("Count 'e':", email.count("e"))
print("Starts with 'User'?", email.startswith("User"))
print("Ends with '.COM'?", email.endswith(".COM"))

# Loop through string
for ch in text:
    print(ch, end=" ")
print()

# String formatting
name = "Sumyya"
score = 92
print(f"Name: {name}, Score: {score}")
print("Name: {}, Score: {}".format(name, score))