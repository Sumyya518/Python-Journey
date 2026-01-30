# ======================================================
# MODULE 6: FILE HANDLING
# ======================================================
print("\n--- MODULE 6: FILE HANDLING ---")

# Write file
with open("sample.txt","w") as f:
    f.write("Hello Python File Handling\n")
    f.write("Learning Python is fun!\n")

# Read file
with open("sample.txt","r") as f:
    print(f.read())

# Append file
with open("sample.txt","a") as f:
    f.write("Appended line.\n")
