import math
radius = float(input("Enter the radius of the circle : "))
circumference = 2*radius*math.pi
print("Actual circumference : ",circumference)
print("Ceil circumference : ",math.ceil(circumference))
print("Floor circumference : ",math.floor(circumference))
print("Rounded circumference : ",round(circumference,2))
