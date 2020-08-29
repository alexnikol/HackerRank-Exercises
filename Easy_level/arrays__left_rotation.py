# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example,
# if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
# Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array
# to be printed as a single line of space-separated integers.

def rotLeft(a, d):
    length = len(a)
    result = [0] * length
    for index, item in enumerate(a):
        newIndex = index - d
        if newIndex < 0:
            newIndex = newIndex + length
        result[newIndex] = item
    return result


a = [1, 2, 3, 4, 5]
d = 2
result = rotLeft(a, d)
print(result)