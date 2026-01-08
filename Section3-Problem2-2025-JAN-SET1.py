
with open(filename, 'r') as file:
    for line in file:
        # Split the line into the string and indices
        parts = line.strip().split(',')
        original_string = parts[0]
        indices = list(map(int, parts[1:]))

        # Rearrange the string based on indices
        rearranged_string = ''.join(original_string[i - 1] for i in indices)
        print(rearranged_string)

# #Another Method:

# with open(filename,'r') as file:
#     s=''
#     for line in file:
#         l=line.rstrip().split(',')
#         for i in range(1,len(l)):
#             num=int(l[i])
#             s += l[0][num-1]
#         print (s)
#         s=''

# String Rearrangement
# Write a program that takes a text file with several lines. Each line has a string followed by indices separated by commas. The function should rearrange the characters in the string according to the given indices and print the updated strings.

# The indices specify the new order of characters in the string.
# Each number corresponds to the position (1-based index) in the original string.
# NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

# Examples

# Input

# hello,2,1,3,5,4
# abcdef,3,2,1,6,5,4
# xyz,3,1,2
# Output

# ehlol
# cbafed
zxy
