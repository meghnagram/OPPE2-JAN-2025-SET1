def add_middle_elems_to_ends_in_even_length_tuple(t: tuple) -> tuple:
    '''
    Given an even-length tuple, rearranges it by placing the two middle elements 
    at the beginning and the end.

    Eg.
    add_middle_elems_to_ends_in_even_length_tuple((10, 20, 30, 40)) 
    -> (20, 10, 40, 30)
    
    add_middle_elems_to_ends_in_even_length_tuple(("Lenovo", "Dell", "HP", "Asus")) 
    -> ("Dell", "Lenovo", "Asus", "HP")

    Args:
        t (tuple): Input tuple of even length.

    Returns:
        tuple: Rearranged tuple with the two middle elements at the ends.
    '''
    
    
    mid = len(t) // 2
    first_middle = t[mid - 1]
    second_middle = t[mid]

    # Rearrange the tuple by placing the middle elements at the ends
    return (first_middle,) + t[:mid - 1] + t[mid + 1:] + (second_middle,)
    
# #Another Method:

# def add_middle_elems_to_ends_in_even_length_tuple(t: tuple) -> tuple:
   
#     tuple_len=len(t) 
  
#     index_first_mid=tuple_len//2-1
  
#     index_second_mid=tuple_len//2
    
#     l=[t[index_first_mid],t[index_second_mid]]
   
#     new_list=[l[0]]+list(t[0:index_first_mid])+list(t[index_second_mid+1:])+[l[1]]
#     return tuple(new_list)    

# Rearrange Even Length Tuple by Placing Middle Elements at Ends
# Write a function add_middle_elems_to_ends_in_even_length_tuple that takes a tuple of even length and performs the following operations:

# Extract the two middle elements.
# Place the first middle element at the beginning and the second middle element at the end.
# Return the newly rearranged tuple.
# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# Example
# add_middle_elems_to_ends_in_even_length_tuple((10, 20, 30, 40)) → (20, 10, 40, 30)
# add_middle_elems_to_ends_in_even_length_tuple(("Lenovo", "Dell", "HP", "Asus")) → ("Dell", "Lenovo", "Asus", "HP")

