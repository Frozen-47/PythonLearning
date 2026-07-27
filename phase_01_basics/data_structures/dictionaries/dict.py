d = {"name": "Sabareesh", "age": "19", 2: "two"}

print(d.get("name"))

s = d.copy()
print(s)

print(d.popitem())
print(d)

d.update(s)
print(d.get('x',1))


