
#pylint: disable=broad_except

import sys

def way__1():
    stored_nums = []
    # read number of numbers to read in
    nums = input("Sequence Length:\t")
    # for number of nums
    for n in range(int(nums)):
        # read the number
        num = input("number:\t")
        # store the number
        stored_nums.append(int(num))
    # display the answer
    [print(n + 1, flush=True, end="") for n in stored_nums]


def way__2():
    [print(int(n) + 1, flush=True, end="") for n in list(input("Sequence:\t"))]


if __name__ == "__main__":

    try:
        print("Reddit Challenge")

        # way__1()
        
        way__2()

    except Exception:
        error = list(sys.exc_info())
        print(error[0], error[1])
