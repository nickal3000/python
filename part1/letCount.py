# H.P Compton
# 2/13/24
# count how many times a letter goes

word = str(input("Enter a word: ").lower())

wordA = list(word)

array = [0] * len(word)

for i in range(0, len(word)):
    for i2 in range(0, len(word)):
        if word[i] == wordA[i2]:
            array[i] += 1
             

count = 0
for char1 in word:
    print(f"{char1} : {array[count]}")
    count += 1


