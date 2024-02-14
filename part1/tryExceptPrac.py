# H.P Compton
# 1/26/24
# This is to practice finding specfic errors with try except
# This will be done with a division calculator 
import PySimpleGUI

try:
    top = int(input("Enter the numerator: "))
    bot = int(input("Enter the denominator: "))

    ans = top / bot

    print(f"The result of {top} divided by {bot} is {ans}")

except ValueError:

    print("Invalid input use a number")

except ZeroDivisionError:

    print("You can not divide by zero")

except:

    print("Unknown error")
