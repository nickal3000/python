# H.P Compton
# 1/25/24
# A diffrent way of doing it
count = 0

total = int(input("Enter your starting population: "))
growR = int(input("Enter the Growth Rate: "))
timeGrow = int(input("How long does this rate take in hours: "))
totalTime = int(input("Over what period: "))

for i in range(0,totalTime,timeGrow):
    total = total * growR
    count += 1

print(f"After {count} cycles the total population is {total}")