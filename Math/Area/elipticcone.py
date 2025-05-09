import math
from math import pi
print('Calculate the area of an eliptic cone.')
x = float(input("Enter the semi major axis: "))
y = float(input("Enter the semi minor axis: "))
z = float(input("Enter the slant height: "))
a = (pi*x*y)+(pi*x*(math.sqrt(z*z-x*x)))
print(f"The answer is {a}")