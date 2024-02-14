# H.P Compton
# 1/30/24
# Enter test scores then average them

count = int(0)
total = int(0)
cont = 'Y'


while True:
    if count != 0:
        cont = input("Would you like to enter another score (Y/N)")
    if cont == "Y" or cont == "y":
        count += 1
        total += int(input("Enter test score: "))
    elif cont == "N" or cont == "n":
        break

print(f"The total of of all test scores is {total}")

print(f"The average score of all {count} is {total / count}")