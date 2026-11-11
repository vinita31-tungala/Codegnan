# Bubble Sort - Swapping the beside elements by increasing order(sorting done from right side(back side) of array values)
'''def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,3,2,4,1]
print(bubble_sort(arr))'''  #Output:[1,2,3,4,5]

# Selection Sort - Finds the smallest element in unsorted portion and swap it with the first unsorted element.(sorting done from left side of array values)
'''def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[5,1,2,4]
print(selection_sort(arr))'''  #Output:[1,2,4,5]

# Insertion Sort - Take one element at a time and insert it into it's correct position in the already sorted portion of array
'''def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,3,6,2,1]
print(insertion_sort(arr))'''  #Output:[1,2,3,5,6]


# Merge sort

'''def merge_sort(arr):
    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide array into two parts
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5, 3, 4, 1, 2]
print(merge_sort(arr))
'''

# Quick Sort
'''def quick_sort(arr):
    if len(arr)<=1:
        return arr
    #n=len(arr)
    #index=n//2
    #pivot=arr[index]  #or
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)
arr=[5,3,6,7,1,4,2]
print(quick_sort(arr))'''