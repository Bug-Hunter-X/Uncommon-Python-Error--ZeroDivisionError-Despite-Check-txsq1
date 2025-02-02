# Uncommon Python Error: ZeroDivisionError Despite Check

This repository demonstrates a subtle error in Python where a `ZeroDivisionError` occurs even though a check for zero is in place.  The issue highlights the importance of careful code structure to prevent such exceptions.

The `bug.py` file contains the erroneous code.  The `bugSolution.py` demonstrates the solution.  The core problem is that the return statement evaluates the 1/x before fully handling the zero condition.

## Solution
The solution is to restructure the conditional statement to ensure the division only happens when x is not equal to zero.