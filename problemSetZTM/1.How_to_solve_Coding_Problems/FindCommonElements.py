# Given 2 arrays create a funciton that lets user know whether these 2 arrays have any elements in common

# NaiveApproach:

ar1 = ['a', [], 'z' 'd', 'x']
ar2 = ['m', 'n', 'o', 'p', []]


def check_common_elements(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False


# print(check_common_elements(a,b))

# complexity = O(a*b) if a size=bsize -then o(n^2)

# Better solution
# creating a map for the first array:
# then check if elements of second are in map.
# if yes retrun true
# else return false
# possible bigO(asize + O(1) for n times)

# code:
def check_common_elements_better(a, b):
    dict1 = {}
    for x in range(0, len(a)):
        if len(dict1) == 0 or dict1.get(x) is None:
            dict1[x] = a[x]
        else:
            continue

    for x in b:
        if x in dict1.values():
            return True
    return False


print(check_common_elements_better(ar1, ar2))

# Step By Step:
# 1. check for what is said in question
# 2. Write inputs / parametrs what is expected
# 3. write what is the output expected results
# 4. write the expected results with examples
# 5.what is the main goal:  time , space
# 6. Since we have all the info required now, start with Naive aproach/BruteForce
# 7. Code if you have time for brute Force otherwise just imagine and write the big(o)
# 8 think of a better solution and try to form what we need to do . dont code yet.
