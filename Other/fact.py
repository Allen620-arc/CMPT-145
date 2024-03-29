# CMPT 145 LabVCS: Version Control
#

def factorial(n):
    """
    Purpose:
        Calculate the factorial of a non -negative integer.
    Pre-conditions:
        n: non-negative integer.
    Return:
        A non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)