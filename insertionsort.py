def insertion_sort(arr):
    """
    This function implements the insertion sort algorithm.
    It takes a list 'arr' and sorts it in-place in ascending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be positioned
        j = i - 1  # Start comparing with the previous element
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key in its correct position
    return arr
