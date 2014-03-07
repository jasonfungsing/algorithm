__author__ = 'jasonfungsing'


def find_max_crossing_subarray(array, low, mid, high):
    left_sum = None  # set it to minus infinite
    sum1 = 0
    max_left = 0
    for i in range(mid, low - 1, -1):
        sum1 = sum1 + array[i]
        if None == left_sum:
            left_sum = sum1
            max_left = i
        elif sum1 > left_sum:
            left_sum = sum
            max_left = i

    right_sum = None  # set it to minus infinite
    sum2 = 0
    max_right = 0
    for j in range(mid + 1, high - 1):
        sum2 = sum2 + array[j]
        if None == right_sum:
            right_sum = sum2
            max_right = j
        elif sum2 > right_sum:
            right_sum = sum2
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(array, low, high):



array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print str(find_max_crossing_subarray(array, 0, 7, len(array)))