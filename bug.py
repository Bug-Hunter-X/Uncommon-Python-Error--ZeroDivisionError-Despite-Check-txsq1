def function_with_uncommon_error(x):
    if x == 0:
        return 1/x # ZeroDivisionError
    else:
        return 1/x

print(function_with_uncommon_error(0))