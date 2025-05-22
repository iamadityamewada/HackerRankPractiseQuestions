# ✅ What is List Comprehension in Python?
# List comprehension is a concise and readable way to create lists in Python.

# It allows you to build a new list by applying an expression to each item in a sequence (like a loop), optionally filtering items with a condition — all in one line.

# 📌 Basic Syntax:
# [expression for item in iterable if condition]
# expression: the value to store in the new list.

# for item in iterable: loop through items.

# if condition: optional; filters which items to include.

# Let's learn about list comprehensions! You are given three integers 
#  and  representing the dimensions of a cuboid along with an integer .
#  Print a list of all possible coordinates given by  on a 3D grid where 
# the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example




# All permutations of  are:
# .

# Print an array of the elements that do not sum to .


# Input Format

# Four integers  and , each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    res = [[i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i+j+k!=n
    ]
    print(res)

