# H.P Compton
# 1/30/24
# take the 3 sides of a tri and find the area

import math

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)