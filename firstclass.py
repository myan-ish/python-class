import math
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

if b**2 < (4*a*c):
	print("The given equation has no real solution.")
else:
	x1 = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)

	x2 = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)


print("The two solution are :", x1, x2)