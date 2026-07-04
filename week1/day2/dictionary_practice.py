student = {
    "name": "John",
    "age": 20,
    "grade": 95
}

print(student["name"])

student["grade"]= 100

student["city"]="New York"

student.pop("age")

for key, value in student.items():
    print(f"{key}:{value}")
    
students = [
    {"name": "John", "grade": 90},
    {"name": "Sarah", "grade": 100},
    {"name": "Mike", "grade": 82}
    ]

for s in students:
    print(f"{s['name']}-{s['grade']}")



