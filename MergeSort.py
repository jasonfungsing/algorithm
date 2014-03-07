__author__ = 'jasonfungsing'


# Top-down merge sort

# devide
def mergeSort(input):
    inputSize = len(input)
    if inputSize == 1:
        return input
    else:
        midIndex = inputSize / 2
        left = []
        right = []
        for i in range(0, midIndex):
            left.append(input[i])
        for i in range(midIndex, inputSize):
            right.append(input[i])
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

# conquer
def merge(left, right):
    result = []
    while (len(left) > 0 and None != left) or (len(right) > 0 and None != right):
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif None != left and len(left) > 0:
            result.append(left[0])
            left.pop(0)
        elif None != right and len(right) > 0:
            result.append(right[0])
            right.pop(0)

    print result
    return result


input = [5, 2, 4, 6, 1, 3]
print "input:" + str(input)
output = mergeSort(input)
print "output:" + str(output)


