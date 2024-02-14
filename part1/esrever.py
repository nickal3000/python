# H.P Compton
# 2/13/24
# take input from user and reverse it

words = str(input("Enter what you want reversed: "))

wordArray = list(words)

rever = words[::-1]
print(rever)

for i in range((len(wordArray)-1), -1, -1): # start num, end num, count by num
    print(wordArray[i], end="")
