age = int(input("Enter Your Age: "))

# Check the condition & show result
if age > 18:
    print("You can drive")
elif age == 18:
    print("You need to visit RTO")
else:
    print("You can't drive")
