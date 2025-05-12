#!/usr/bin/python3
# Write a function that divides element by element 2 lists.
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(0, list_length):
        try:
            result = (my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except Exception:
            result = 0
        finally:
            new.append(result)
    return new
