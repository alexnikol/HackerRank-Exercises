# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people
# queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions
# increment by 1 from 1 at the front of the line to n at the back.
# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap
# positions, they still wear the same sticker denoting their original places in line. One person can bribe
# at most two others. For example, if n = 8 and Person 5 bribes Person 4, the queue will look like
# this: 1, 2, 3, 4, 5, 6, 7, 8.
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place
# to get the queue into its current state!
# Function Description
# Complete the function minimumBribes in the editor below. It must print an integer representing
# the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
# minimumBribes has the following parameter(s):


def minimumBribes(q):
    bribesCount = 0
    for i in range(len(q), 0, -1):
        itemIndex = i - 1
        if q[itemIndex] == i:
            continue
        elif q[itemIndex - 1] == i:
            bribesCount += 1
            q[itemIndex - 1] = q[itemIndex]
            q[itemIndex] = i
        elif q[itemIndex - 2] == i:
            bribesCount += 2
            q[itemIndex - 2] = q[itemIndex - 1]
            q[itemIndex - 1] = q[itemIndex]
            q[itemIndex] = i
        else:
            print("Too chaotic")
            return
    print(bribesCount)


minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])


