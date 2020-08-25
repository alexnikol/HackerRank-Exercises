# HackerRank exercise https://www.hackerrank.com/challenges/sparse-arrays/problem
# Data Structures -> Arrays -> Sparse Arrays

def matchingStrings(strings, queries):
    result = []
    for i in range(0, len(queries)):
        result.append(0)
    for index, query in enumerate(queries):
        for item in strings:
            if query == item:
                result[index] += 1
    return result


result = matchingStrings(["ab", "ab", "abc"], ["ab", "abc", "bc"])
print(result)
