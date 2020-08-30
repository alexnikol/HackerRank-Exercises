# https://www.hackerrank.com/challenges/swap-case/problem
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to
# uppercase letters and vice versa. For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def swap_case(s):
    result = ""
    for i in s:
        if i.islower():
            result += i.upper()
        elif i.isupper():
            result += i.lower()
        else:
            result += i
    return  result


swap_case("Www.HackerRank.com")



