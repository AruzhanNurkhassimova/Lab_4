#1
import math
n=int(input("Input degree: "))
radian=math.radians(n)
print("Output radian: ", round(radian,6))


#2
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
A=(a+b)/2*h
print("Expected Output: ", A)


#3
import math
n=int(input("Input number of sides: "))
s=int(input("Input the length of a side: "))
a=s/(2*math.tan(math.pi/n))
A=(n*s*a)/2
print("The area of the polygon is: ", A)


#4
b=float(input("Length of base: "))
h=float(input("Height of parallelogram: "))
A=b*h
print("Expected Output: ", A)
