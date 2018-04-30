

def sum_int(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise RuntimeError("invalid integer(s)")
    return num1 + num2
