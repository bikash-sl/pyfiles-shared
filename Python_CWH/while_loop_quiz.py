while True:
    num = float(input("Enter the number: "))
    if num <= 100:
        print("You have entered:", str(num), "\n")
    else:
        print("You have entered a number greater than 100")
        break
