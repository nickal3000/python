
import random

m1 = input("Enter your first movie: ")
m2 = input("Enter your second movie: ")
m3 = input("Enter your third movie: ")


num = random.randint(1,3)

mov = ""

if num == 1:
    mov = m1
if num == 2:
     mov = m2
if num == 3:
    mov = m3

print(mov)