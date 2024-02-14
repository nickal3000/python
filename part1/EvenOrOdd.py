# H.P Compton
# 1/25/24
# practice of f strings solving if a number is even or odd


while True:




    try:
        num = int(input("Enter a number: "))
        print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}")


    except:
        print("Invalid input")
        break
