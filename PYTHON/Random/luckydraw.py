import random
students={
"Ritik":85,
"Rahul":78,
"Aman":92,
"Rohit":88,
"Ankit":75,
}

name = input("Enter student name: ")
marks =int(input("Enter marks: "))
students[name]=marks

print(students)
