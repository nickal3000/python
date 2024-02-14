# addes indefinite ints until enter

counter = 0
total = int(0)


while True:
    counter += 1

    temp = input("Enter number: ")

    if temp != "":
        total += int(temp)

    else:
       break


print(total)