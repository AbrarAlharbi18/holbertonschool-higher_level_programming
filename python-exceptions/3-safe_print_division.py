#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.
def safe_print_division(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        answer = None
    except Exception:
        answer = None
    finally:
        print("Inside result: {}".format(answer))
        return answer
