"""
Write a program to fill in a letter template given below with name and date.

Dear <|Name|>,
    You are selected !
    <|Date|>
"""


style_1 = '''Dear <Name>,
\tYou are selected !
Date: <Date>'''


name = input("Enter your Name: ")
dt = input("Enter Date: ")


style_1 = style_1.replace("<Name>", name)
style_1 = style_1.replace("<Date>", dt)


print("\n" + style_1)
