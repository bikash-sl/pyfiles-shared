"""
Create a list of your favorite things, and then use pickle to save
them to a file called favorites.dat. Close the Python shell, and then
reopen it and display your list of favorites by loading the file.
"""

import pickle

myfav = ["Super man", "Spider man", "Captain America",
         "Flash", "Iron man", "Goku", "Doraemon"]

# Dumping(writting) myfav list to the Favorite.dat file
favorite = open("Favorite.dat", "wb")
pickle.dump(myfav, favorite)
favorite.close()
print("Data Written Successfully.\n")

# Retrieve process
favorite = open("Favorite.dat", "rb")
load_data = pickle.load(favorite)
favorite.close()

print(load_data)
print("\nData retrievation Successfull.")
