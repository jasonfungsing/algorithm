__author__ = 'jasonfungsing'


def insertionSort(input):
    print "Input: " + str(input)
    counter = 0
    size = len(input)
    for i in range(1, size):
        counter += 1
        key = input[i]

        j = i - 1
        while j >= 0 and input[j] > key:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = key
        print str(counter) + " #: " + str(input)

    print "Output: " + str(input)
    return input


input = [5, 2, 4, 6, 1, 3]
insertionSort(input)