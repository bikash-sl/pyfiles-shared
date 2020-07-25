"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers.

Sample data : 3, 5, 7, 23
Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
"""

sample_data = input("Enter some numbers separated by comma: ")

lst = sample_data.split(",")
print("List: ", lst)
print("Tuple: ", tuple(lst))

input("\nPress Enter to exit ... ... ... ")
