def binary_search(array,target):
    min = 0
    max = len(array) - 1
    guess = 0
    while max > min:
        guess = (max + min // 2)
        if array[guess] == target:
            return guess
        elif array[guess] > target:
            max = guess - 1
        else:
            min = guess + 1
    return -1
array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binary_search(array, 71))
