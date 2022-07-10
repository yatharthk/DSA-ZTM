ar = [1, 2, 4, 4]
k = 8


# Brute Force way with BigO(n^2) Time and space as BigO(1)
def brute_force_pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == sum:
                return True
    return False


# calculate the compliment and use a binary search for further elements
# Check if complement is present or not on the remaining array
# Given array is sorted

def binary_search(array, left, right, ele):
    if right >= left:
        mid = (left + right) // 2
        if (array[mid]) == ele:
            return True
        elif array[mid] > ele:
            return binary_search(array, left, mid - 1, ele)
        else:
            return binary_search(array, mid + 1, right, ele)
    else:
        return False


def slightly_better_pair_sum(array, sum):
    for i in range(len(array)):
        comp = sum - array[i]
        if binary_search(array, i + 1, len(array) - 1, comp):
            return True
    return False


# print(slightly_better_pair_sum(ar, k))
# Time: BigO(nlog n)

# Smart pairing  assuming array is still sorted
def smart_pair_sum(array, sum):
    left = 0
    right = len(array) - 1
    while right > left:
        if array[left] + array[right] == sum:
            return True
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return False


# print(smart_pair_sum(ar, k))


# Time Complexity: BigO(n)

# Q:What if array is not sorted.?
# ans: lets sort it and again follow same
def sort_pair_sum(array, sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while right > left:
        if array[left] + array[right] == sum:
            return True
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return False


# print(sort_pair_sum(ar,k))
# Time : BigO(n* log n) :( .

# Let's create a dictionary and try it once :
def smartest_pair_sum(array, sum):
    dictionary = dict()
    for item in array:
        compliment = sum - item
        print(item,compliment)
        if compliment not in dictionary:
            dictionary[item] = True
        else:
            return True
    return False


print(smartest_pair_sum(ar, k))
# finally BigO(n)