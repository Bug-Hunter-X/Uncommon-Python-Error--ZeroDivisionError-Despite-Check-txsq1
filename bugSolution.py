def function_with_uncommon_error_solution(x):
    if x != 0:
        return 1/x
    else:
        return float('inf') # Handle zero division with Infinity or another suitable value

print(function_with_uncommon_error_solution(0))