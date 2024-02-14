# H.P Compton
# 2/13/24
# check if string 1 and two have same letters

count = 0

word1 = str(input("Enter word 1: "))
word2 = str(input("Enter word 2: "))
a1 = list(word1.lower())
a2 = list(word2.lower())



for i in range (0, len(word1)):
    for i2 in range(0,len(word2)):
        if i == i2:
            count += 1
            a2[i2] = ''

if count == len(word1):
    print("The words are balanced")
else:
    print("The words are not balanced")




