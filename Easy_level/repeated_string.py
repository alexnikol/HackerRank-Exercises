# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Repeated String


def repeatedString(s, n):

    def find_repeats_a_in_string(string):
        a_count = 0
        for letter in string:
            if letter == "a":
                a_count += 1
        return a_count

    letters = len(s)
    full_repeats = n // letters
    last_part_count = n % letters
    result = 0
    last_part_string = s[0:last_part_count]
    if full_repeats > 0:
        result += find_repeats_a_in_string(s) * full_repeats
    if last_part_count > 0:
        result += find_repeats_a_in_string(last_part_string)
    return result


print(repeatedString("aba", 10))
