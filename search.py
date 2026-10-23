# Searching Algorithms:
# 1. Linear Search :
# --->It search elements one by one.
# --->It works on sorted and unsorted array
# --->Time Complexity->Best case-O(1)
# --->Average case->O(N)
# --->Worst case->O(N)

'''def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,47,27,59,90]
target=90
result=linear_search(arr,target)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")'''

# 2. Binary Search :
# --->Divide and Conquer
# --->It works on sorted array

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [10, 20, 30, 40, 50]
target = 10

result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

