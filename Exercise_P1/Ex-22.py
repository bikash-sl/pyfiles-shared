# 22. Write a Python program to count the number 4 in a given list.

my_lst = [4, 6, 3, 13, 65, 4, 32, 4, 64]

count_fours = 0

for i in my_lst:
    if i == 4:
        count_fours += 1

print("Number of 4(s) in the list is", count_fours)

input("\nPress Enter to exit ... ... ... ")
