# OOPs in Python 
# OOP- Object Oriented Programming

# using list - creating student records
# student details
student_1 = ['Madhav', 10] # Name, Grade
student_2 = ['Vishakha', 12] 
student_3 = 'Keshav'

student_1.append('A')
print(student_1)
print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')


# using OOPs- creating student records

# class - blueprint or template
# __init__ method - constructor, value initialize - fix
# self parameter - reference or connection build btw class and object - fix
class Student: # student class
    def __init__(self, name, grade, percentage):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class 
student1 = Student('Madhav', 11, 96)
print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
print(student2.name, student2.grade)

print(student1.percentage)
student1.student_details()
student2.student_details()

print(student1.__dict__) 

# modify object property
print(student1.percentage) 
student1.percentage = 100 # modify
print(student1.percentage)

# delete object property 
print(student1.__dict__) 
del student1.percentage
print(student1.__dict__) 

# delete object 
del student1
print(student1)



# class - blueprint or template
class Student: # student class
    def __init__(self, name, grade, percentage, team):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute
        self.team = team

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is in team {self.team}")

team1 = 'A'
team2 = 'B'

# object - instance of class 
student1 = Student('Madhav', 11, 96, team1)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99, team2)
# print(student2.name, student2.grade)

# print(student2.team)
student1.student_details()
student2.student_details()