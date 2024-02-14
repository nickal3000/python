# H.P Compton
# 1/30/24
# convert to C or F choosen by user


choice = input("Would you like to convert to Fahrenheit or Celsius (F/C): ")

temp = int(input("Enter the number you would like to convert: "))

if choice == "f" or choice == "F":
    print(f"{temp} in fahrenheit is {round((temp * (9/5))+32, 2)}")
elif choice == "c" or choice == "C":
    print(f"{temp} in celsius is {round((temp-32) * (5/9),2)}")
