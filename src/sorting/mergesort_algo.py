from typing import Callable

""" Basic quicksort implementation

This quicksort implementation selects the last element of the array as a pivot for the array partitioning for the
subsequent recursive sorting of:
 - sub-array with elements smaller than the pivot, and
 - sub-array with elements greater than the pivot

This implementation has an average time complexity of O(n·log n). Best case complexity is also O(n·log n).
However, worst case performance of this implementation is O(n^2), and it takes places on arrays already
sorted in increasing or decreasing order.

Other quicksort implementations overcome this issue by selecting as pivot:
 - middle element in the array
 - median element
 - a random element
"""


def __default_comparer(a, b):
    return a < b


def mergesort(arr: list, compare_func: Callable = __default_comparer) -> None:
    """
    Performs quicksort sorting over the chunk [low:high] of a given array.

    :param arr: (list) Input array
    :param compare_func (Callable) Function to compare elements inside the array
    """
    if len(arr) <= 1:
        return

    # Split the array in two
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Sort left and right chunk
    mergesort(left_arr, compare_func)
    mergesort(right_arr, compare_func)

    # Sort elements in destination array
    left_idx = 0
    right_idx = 0
    dest_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        compare_result = compare_func(left_arr[left_idx], right_arr[right_idx])
        if compare_result:
            arr[dest_idx] = left_arr[left_idx]
            left_idx += 1
        else:
            arr[dest_idx] = right_arr[right_idx]
            right_idx += 1
        dest_idx += 1

    # Add remaining elements in left array if any
    while left_idx < len(left_arr):
        arr[dest_idx] = left_arr[left_idx]
        left_idx += 1
        dest_idx += 1

    # Add remaining elements in right array if any
    while right_idx < len(right_arr):
        arr[dest_idx] = right_arr[right_idx]
        right_idx += 1
        dest_idx += 1
