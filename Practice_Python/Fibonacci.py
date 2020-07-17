"""
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. (use functions)
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of
the previous two numbers in the sequence.
The sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, …)
"""


def fiboseq(nth_term):
    """The function will return a fibonacci sequence for nth no. of term"""

    fibo_list = [0, 1]
    if nth_term <= 0:
        print("Length must be a positive integer.")
        fibo_list.clear()
    elif nth_term == 1:
        fibo_list = [fibo_list[0]]
    elif nth_term == 2:
        pass
    else:
        counter = 1
        while counter < nth_term-1:
            fibo_list.append(fibo_list[-1] + fibo_list[-2])
            counter += 1

    return fibo_list


def fiboval(num):
    """The function will return a fibonacci value of the number"""

    if num < 0:
        return None
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fiboval(num-1) + fiboval(num-2)


if __name__ == "__main__":

    op_type = int(input("Enter [1] for Fibonacci series"
                        " [2] to get Fibonacci value: "))

    if op_type == 1:
        length = int(input("Enter the length of fibonacci series you want: "))
        print("Fibonacci sequence:")
        print(*fiboseq(length), sep=", ")
    elif op_type == 2:
        index_num = int(input("Enter the number to get Fibonacci value: "))
        print(f"Fibonacci value of {index_num} is {fiboval(index_num)}.")

    input("\nPress Enter to exit ..... ")
