


def add_value(value):
    # Base case: stop recursion when the value is less than 0
    if value < 0:
        return None

    # Recursive case: increment the value and call the function again
    SUM = value + 1
    print(SUM)

    # Call add_value recursively with a decremented value
    value = value - 1
    return add_value(value)



if __name__ =="__main__":
    print(add_value(7))