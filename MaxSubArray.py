__author__ = 'jasonfungsing'


def find_max_crossing_subarray(array, low, mid, high):
    left_sum = None
    sum1 = 0
    max_left = 0
    for i in range(mid, low - 1, -1):
        sum1 = sum1 + array[i]
        if None == left_sum:
            left_sum = sum1
            max_left = i
        elif sum1 > left_sum:
            left_sum = sum1
            max_left = i

    right_sum = None
    sum2 = 0
    max_right = 0
    for j in range(mid + 1, high + 1):
        sum2 = sum2 + array[j]
        if None == right_sum:
            right_sum = sum2
            max_right = j
        elif sum2 > right_sum:
            right_sum = sum2
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(array, low, high):
    mid = (low + high) / 2
    if high == low:
        return (low, high, array[low])
    else:
        (left_low, left_high, left_sum) = find_max_subarray(array, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(array, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(array, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)


# array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
array = [-3, 2, -5, 10, -2, 8, -8, 1, 4]
print str(find_max_subarray(array, 0, len(array)-1))
