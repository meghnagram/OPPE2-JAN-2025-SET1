def count_strings_length_divisible_by_3_or_5(strings: list) -> int:
    """
    Counts how many strings in a list have lengths divisible by either 3 or 5.

    Args:
        strings (list[str]): List of strings.

    Returns:
        int: The count of strings with lengths divisible by either 3 or 5.
    
    Examples:
        >>> count_strings_length_divisible_by_3_or_5(["misunderstanding", "inconsiderately", "acknowledgement"])
        2
        >>> count_strings_length_divisible_by_3_or_5(["coding", "algorithm", "development"])
        2
    """
    
    
    return sum(
        len(string) % 3 == 0 or len(string) % 5 == 0 
        for string in strings
    )

# #Another Method:
# def count_strings_length_divisible_by_3_or_5(strings: list) -> int:
    
#     count=0
#     for i in strings:
#         if len(i)%5==0 or len(i)%3==0:
#             count +=1
#     return count

# Count Strings with Length Divisible by Either 3 or 5
# Write a function count_strings_length_divisible_by_3_or_5(strings) that takes a list of strings and counts how many strings have lengths divisible by either 3 or 5.

# Examples

# strings = [
#     "misunderstanding", "inconsiderately", 
#     "characters", "computers"
# ]
# print(count_strings_length_divisible_by_3_or_5(strings)) # Output: 3
# Explanation

# "misunderstanding" has 16 characters which is not divisible by either 3 or 5. Thus not counted.
# "inconsiderately" has 15 characters which is divisible by both 3 and 5. Thus counted.
# "characters" has 10 charaters which is divisible by 5. Thus counted
# "computer" has 9 characters which is divisible by 3. Thus counted.
    
