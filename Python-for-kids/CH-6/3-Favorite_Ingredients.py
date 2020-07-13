'''
Create a list containing five different sandwich ingredients
Now create a loop that prints out the list (including the Sl. numbers)
'''

ingredients = ["snails", "leeches", "gorilla belly-button lint",
               "caterpillar eyebrows", "centipede toes"]

for item in ingredients:
    print(ingredients.index(item)+1,  item)
