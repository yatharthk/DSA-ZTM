# Given the list of numbers find the pair which matches to the given sum

# //Inputs: A array say a
# Expected output = Pair exists that sums up to given sum say k

# Naive Soluiton:
# Step 1 Loop through the element 1
# Step2 make an internal loop that again loops the same array
# Step 3 check if the sum matches k
# if yes return true else return false

# Code

array = [1, 2, 3, 9]
desired_sum = 8

arr2 = [1,2,3,4,4]


def check_if_pair_exists(a, k):
    for x in range(0, len(a)):
        for y in range(1, len(a)):
            if a[x] + a[y] == k:
                return True
    return False


# time comp: O(n^2)
# space comp: O(1) (: since no extra ds created using pre declared variables thus constant

# print(check_if_pair_exists(arr, desired_sum))
# print(check_if_pair_exists(arr2, desired_sum))


# Better_Solution

# Use map and insert the complement of the number
# proceed forwards if this number encounters then sum pair found else return not found

def check_if_pair_exists1(arr, sum):
    dict2 = {}
    for x in arr:
        if len(dict2) == 0 or dict2.get(x) is None:
            dict2[x] = sum - x
            print(dict2)
        # elif dict2.get(x)+x == sum:
        #     return True
    for y in arr:
        if y in dict2.values():
            print(dict2.get(x), x)
            return True
    return False

    # if arr in dict2.values():
    #     return True
    # return False



print(check_if_pair_exists1(arr2, desired_sum))
# time comp: O(a+b)
