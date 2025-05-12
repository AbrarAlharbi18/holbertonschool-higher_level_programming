#!/usr/bin/python3
# Write a function that prints the first x elements of a list and only integer
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    real_value = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count = count + 1
        except ValueError:
            count = count + 1
            real_value += 1
            continue
        except TypeError:
            count += 1
            real_value += 1
    print()
    return count - real_value
