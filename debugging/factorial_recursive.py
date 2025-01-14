#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given non-negative integer 'n'.
    The factorial of a number is the product of all positive integers less than
    or equal to that number. The function uses recursion to calculate the factorial.
    
    Parameters:
    n (int): A non-negative integer for which the factorial will be computed.
    
    Returns:
    int: The factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))  # Get the factorial of the input argument
print(f)  # Print the result