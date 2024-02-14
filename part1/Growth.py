# H.P Compton
# 1/25/24
# basic answer done not efficiently
hours = 0

total = int(input("Enter your starting population: "))
growR = int(input("Enter the Growth Rate: "))
timeGrow = int(input("How long does this rate take in hours: "))
totalTime = int(input("Over what period: "))

while totalTime > hours:

    total = total * growR
    hours += timeGrow
    print("after " + str(hours) + " the population is " + str(total))