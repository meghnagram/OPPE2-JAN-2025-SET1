

n, t = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(n)]

thresholded_image = [
    ['@' if pixel >= t else '*' for pixel in row] 
    for row in image
]

for row in thresholded_image:
    print(' '.join(row))

# #Another Method


# # Write your code here

# x,y=input().split()
# x=int(x)
# y=int(y)

# while (x!=0):
#     x -=1
#     a=[]
#     s=''
#     a=input().split()
#     for i in a:
#         if int(i) >=y:
#             s=s+'@ '
#         else:
#             s=s+'* '
#     print (s.strip())

# Thresholding a 2D Array and Printing with * and @
# Given an n x n 2D array of integers (0 to 255) and a threshold t, replace each value with @ if it is greater than or equal to t, otherwise replace it with *.

# Input Format

# The first line contains two integers: n (the number of rows of the image) and t (the threshold).
# The next n lines contain n integers (in the range 0-255) for the image.
# Output Format

# Print the thresholded array, each element separated by spaces over multiple lines.
# There should be no space in the begining or the end of each line.
# Word of wisdom: This task is also known as thresholding in image processing. Usually image pixels are represented with values from 0-255.

# Examples

# Input 1

# 3 5
# 7 2 8
# 4 5 3
# 6 0 7
# Output 1

# @ * @
# * @ *
# @ * @ 
# Input 2

# 2 50
# 10 70
# 60 40
# Output 2

# * @
# @ *
