"""
10. Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = int(input("Enter an integer (n): "))
nn = int(2*str(n))
nnn = int(3*str(n))
print("Result of (n+nn+nnn) is: ", n+nn+nnn)

input("\nPress Enter to exit ... ... ... ")
