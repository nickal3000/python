# H.P Compton
# 1/25/24
# This program will take users name and age and tell them how old they will be in 100 years
# And what year that they turn 100


import datetime

thisYear = datetime.datetime.now().year


name = input("Enter your name : ")

bYear = int(input('Hello '+ name +' please enter your birth year'))

print("You are ", thisYear-bYear , " and will be 100 in ", bYear+100)