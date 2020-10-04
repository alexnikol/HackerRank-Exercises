# https://www.hackerrank.com/challenges/crush/problem
# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of
# the array element between two given indices, inclusive. Once all operations have been performed,
# return the maximum value in your array.
# For example, the length of your array of zeros n = 10


def arrayManipulation1(n, queries):
    mapBoard = []
    maxValue = 0

    for i in range(0, n):
        mapBoard.append(0)

    for query in queries:
        leftIndex = query[0] - 1
        rightIndex = query[1] - 1
        value = query[2]

        for index in range(leftIndex, rightIndex + 1):
            mapBoard[index] += value
            if mapBoard[index] > maxValue:
                maxValue = mapBoard[index]

    return maxValue


def arrayManipulation(n, queries):
    result = 0
    mapBoard = []

    for i in range(0, n):
        mapBoard.append(0)

    for a, b, k in queries:
        mapBoard[a - 1] += k
        if b < len(mapBoard):
            mapBoard[b] -= k
    stepSum = 0
    for i in mapBoard:
        if i >= 0:
            stepSum += i
        else:
            if stepSum > result:
                result = stepSum
                stepSum = 0
    return result


result1 = arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
result2 = arrayManipulation(10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]])
print("RESULT 1 " + str(result1))
print("RESULT 2 " + str(result2))




