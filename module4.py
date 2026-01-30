# ======================================================
# MODULE 4: COLLECTIONS (List, Tuple, Set, Dictionary)
# ======================================================
print("\n--- MODULE 4: COLLECTIONS ---")

# LIST
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(1,15)
numbers.remove(30)
numbers.pop()
numbers.sort()
numbers.reverse()
print("List:", numbers)

# List comprehension
squares = [x**2 for x in range(1,6)]
print("Squares:", squares)

# TUPLE
coords = (3,7,10)
print("Tuple:", coords)
x,y,z = coords
print("Unpacked:", x,y,z)

# SET
unique_vals = {1,2,3,4,4,5}
print("Set:", unique_vals)
unique_vals.add(6)
unique_vals.remove(3)
print("Updated Set:", unique_vals)

# Set operations
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# DICTIONARY
student = {"name":"Sara","roll":21,"course":"Python","marks":89}
print("Student dict:", student)
print("Name:", student["name"])
student["marks"]=92
student["grade"]="A"
for key,value in student.items():
    print(key,":",value)
