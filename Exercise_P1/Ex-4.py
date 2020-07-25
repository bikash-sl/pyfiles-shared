"""
4. Write a Python program which accepts the radius of a circle from the user 
and compute the area. 

A = pi * (r)^2
pi = 3.14 or (22/7)

Sample Output :
r = 1.1
Area = 3.8013271108436504
"""


print("\t\tCircle Area Calculator")

radius = int(input("Enter the radius: "))

area = 3.14 * (radius ** 2)

print("Area of the circle is:", area)
