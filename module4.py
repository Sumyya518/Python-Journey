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

# DICTIONARY
student = {"name":"Sara","roll":21,"course":"Python","marks":89}
print("Student dict:", student)
print("Name:", student["name"])
student["marks"]=92
student["grade"]="A"
for key,value in student.items():
    print(key,":",value)
