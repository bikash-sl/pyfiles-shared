numerics = [int, float]
mylist = ["bikash", 24, 8.6, "thor", 7, "iron", 45, 2, 6, 3, 6.5, 35/4]
mynumbers = []

for item in mylist:
    if type(item) in (numerics or str(item).isnumeric()) and item > 6:
        mynumbers.append(item)

# the star unpacks the list and return every element in the list
print(*mynumbers, sep=", ")

# mylist = ["bikash", 24, 8.6,"thor", 7, "iron", 45, 2, 6, 3, 6.5]
# mynumbers = []
#
# for item in mylist:
#     if str(item).isnumeric() and item > 6:
#         mynumbers.append(item)
#
# print(*mynumbers, sep=", ")
