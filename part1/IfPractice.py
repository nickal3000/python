# Hollyday Compton
# 1/18/24
# practice the uses of if and and statements


start = bool(True)

while start:
    score = int(input('enter the score to see your letter grade '))

    if score >= 90:
        
        print('You have an A')

    if score < 90 and score >= 80:
        print('You have a B')

    if score < 80 and score >= 70:
        print('You have a C')

    if score < 70 and score >= 60:
        print('You have a D')

    if score < 60:
        print('You have an F')

    if score == 44:
        break




