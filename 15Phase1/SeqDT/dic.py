
student = {"name": "Rose", "age": 18}
car = {"brand": "Toyota", "year": 2025}
employee = {"id": 101, "salary": 50000}
country = {"India": "New Delhi"}
book = {"title": "Python", "pages": 300}

print(student)
print(car)
print(employee)
print(country)
print(book)

print(student["name"])

student["course"] = "Python"
print(student)

student["age"] = 19
print(student)

print(student.keys())
print(student.values())
print(student.items())