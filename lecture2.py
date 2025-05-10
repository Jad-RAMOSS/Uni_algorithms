def insertion_sort(array, size):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    for j in range(1, size):
        key = array[j]
        i = j-1
        while i>=0 and array[i] > key:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key
    return array


def merge_sort(arr):
    """
    Time Complexity:  O(n log n)
    Space Complexity: O(n)
    """
    n = len(arr)
    if n <= 1:
        return arr[:]  # make a shallow copy

    mid = n // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge the two sorted halves
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # append any remaining tail
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged

def quick_sort(array):
    """
    Complexity: Θ(n²)
    """
    pivot = 0
    i= 1
    j=(len(array)-1)
    while(j>i):
        while array[i] <= array[pivot]:
            i+=1
        while array[j] > array[pivot]:
            j-=1
        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp2 = array[j]
    array[j] = array[pivot]
    array[pivot] = temp2
    pivot = j
    return array
    
array = [4,2,6,1,8,3,5,7,9]


print(insertion_sort(array, len(array)))
print(quick_sort(array))
print(merge_sort(array))
