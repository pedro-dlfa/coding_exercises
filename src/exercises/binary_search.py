def binary_search(arr, k):
    """
    Performs binary search on a given array
    """

    def __binary_search(arr, low, high, k):
        mid_idx = (low + high) // 2
        mid_val = arr[mid_idx]

        if mid_val == k:
            # If found: return true
            return True
        if low == high:
            # If no more elements to search for: return false
            return False

        # If more elements, search in the appropriate half
        if mid_val > k:
            return __binary_search(arr, low, mid_idx, k)
        else:
            return __binary_search(arr, mid_idx + 1, high, k)

    return __binary_search(arr, 0, len(arr), k)
