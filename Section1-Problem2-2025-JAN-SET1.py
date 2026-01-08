def starts_and_ends_with_same_vowel(s: str) -> bool:
    '''
    Given a string, check if it starts and ends with the same vowel (case insensitive).

    Eg.
    starts_and_ends_with_same_vowel("Apple") -> False
    starts_and_ends_with_same_vowel("Atta") -> True
    starts_and_ends_with_same_vowel("Tart") -> False
    starts_and_ends_with_same_vowel("umbrella") -> False

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string starts and ends with the same vowel, else False.
    '''
    
    
    vowels = "aeiouAEIOU"

    # Check if string is empty or has only one character
    if len(s) < 2:
        return False

    # Convert to lowercase for case insensitivity
    s = s.lower()

    return (s[0] == s[-1]) and (s[0] in vowels)

# #Another Method:

# def starts_and_ends_with_same_vowel(s: str) -> bool:
   
#     if s[0].lower()==s[-1].lower() and s[0].lower() in ('aeiou'):
#         return True
#     else:
#         return False

# Check if a String Starts and Ends with the Same Vowel (Case Insensitive)
# Write a function starts_and_ends_with_same_vowel that takes a string as input and returns True if the string starts and ends with the same vowel (case insensitive), otherwise False.

# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# Example
# starts_and_ends_with_same_vowel("Apple") → False (starts with A and ends with e, different vowels)
# starts_and_ends_with_same_vowel("Atta") → True (starts with A and ends with a, same letter and vowel)
# starts_and_ends_with_same_vowel("Tart") → False (starts with T, ends with t, same letter but not vowel)
# starts_and_ends_with_same_vowel("umbrella") → False (starts with u, ends with a, different vowels)
    
