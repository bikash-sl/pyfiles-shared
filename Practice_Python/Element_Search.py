"""
Exercise 20

Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list 
and returns (then prints) an appropriate boolean.

Extras: Use binary search.
"""


def binsearch(array, find):
    """Perform binary search upon an ordered sequence of elements 
    (e.g.: list, tuple, string) in 'array' parameter for the element 
    in 'find' parameter.\n
    Returns boolean value, index no. of the element in the array, if present."""

    bottom = 0
    top = len(array)-1

    # As long as the items are in the array the loop will run
    while bottom <= top:

        # Gets mid point index no. using floor division
        mid = (bottom+top)//2

        # Comparing the mid item with the search item
        if array[mid] == find:
            return True, mid

        # Searching only to the left-side of mid item
        elif array[mid] > find:
            top = mid - 1

        # searching only to the right-side of mid item
        elif array[mid] < find:
            bottom = mid + 1

    return False


if __name__ == "__main__":

    import random

    num_range = random.choice([500, 1000, 1500, 2000])
    random_lst = random.sample(range(num_range), 400)
    ordered_lst = sorted(random_lst)

    print(ordered_lst)
    print(f"\nIt is a random list having {400} items in it.")
    search_elem = int(input("Enter a number you want to search in the list: "))

    search_result = binsearch(ordered_lst, search_elem)

    if search_result:
        print(f"Boolean value is {search_result[0]}.")
        print(
            f"Your item is found at index no. {search_result[1]} in the list.")
    elif not search_result:
        print(f"Boolean value is {search_result}.")
        print("Your item is not in the list.")

    input("Press Enter to exit ... ... ... ")
