#give an intro to the user
print("Let's calculate the area of a Trapezoid")

#ask for information to calcuate the area of the trapezoid
base1 = float(input("What's the value of base1 (a)? "))
base2 = float(input("Whats the value of base2 (b)"))
height = float(input("What's the height?"))

#do the math to calculate the area of the trapezoid
area = (base1 + base2) / 2 * height

#give the final response
print("The area of the Trapezoid is:", area)