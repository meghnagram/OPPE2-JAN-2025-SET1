
def is_multiple(a: int, b: int) -> bool:
    '''
    Given two integers, check if either is a multiple of the other.

    Eg.
    is_multiple(10, 5) -> True
    is_multiple(6, 18) -> True
    is_multiple(7, 3) -> False
    is_multiple(8, 16) -> True

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        bool: True if either is a multiple of the other, else False.
    '''
    
    return (a % b == 0) or (b % a == 0)

# #Another Method:

# def is_multiple(a: int, b: int) -> bool:
    
#     if a%b==0 or b%a==0:
#         return True
#     else:
#         return False

# Check if Either of Two Numbers is a Multiple of the Other
# Write a function is_multiple that takes two integers as input and returns True if either number is a multiple of the other, otherwise False.

# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# Example
# is_multiple(10, 5) → True (10 is a multiple of 5)
# is_multiple(6, 18) → True (18 is a multiple of 6)
# is_multiple(7, 3) → False (neither is a multiple of the other)
# is_multiple(8, 16) → True (16 is a multiple of 8)
    
