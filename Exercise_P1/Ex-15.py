"""
15. Write a Python program to get the volume of a sphere with radius 6.

formula = (4/3) * π * r^3       [π = 3.14]
"""

rad = int(input("Enter the radius of the sphere: "))

volume = (4/3) * 3.14 * (rad ** 3)

print("Volume of the sphere is: %.4f" % volume)

input("\nPress Enter to exit ... ... ... ")
