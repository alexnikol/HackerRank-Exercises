# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen
# In Python, a string can be split on a delimiter.
# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']

def split_and_join(line):
    splited = line.split(" ")
    return "-".join(splited)


print(split_and_join("this is a string"))
