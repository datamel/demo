def summy(arg):
    total = 0
    for val in arg:
        total += val
    return total


def oddy(num):
    if not (isinstance(num, (int, float))):
        raise ValueError
    elif num % 2 == 0:
        return False
    else:
        return True
 
