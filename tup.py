
# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

# Output Format

# Print the result of .

# Sample Input 0

# 2
# 1 2
# Sample Output 0

# 3713081631934410656


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
