# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def jumpingOnClouds(c):
    steps = 0
    activeIndex = 0
    for index, _ in enumerate(c):
        if activeIndex != index:
            continue
        if index + 2 >= len(c):
            break
        next = c[activeIndex + 1]
        nextAfterNext = c[activeIndex + 2]
        if (next == 0 and nextAfterNext == 0) or (next == 1 and nextAfterNext == 0):
            steps += 1
            activeIndex += 2
        elif next == 0 and nextAfterNext == 1:
            steps += 1
            activeIndex += 1
    if activeIndex < len(c) - 1:
        steps += 1
    return steps


print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
