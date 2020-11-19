from typing import Callable

""" Mergesort implementation

Mergesort performs as follows:
 - First, finds a mid point and partitions the array in two halves
 - Then sorts recursively the two halves
 - Finally, places the sorted elements from the two halves in the right order in the array

This implementation has an average time complexity of O(n·log n). Best and worst cases complexity are also O(n·log n).

Mergesort is stable. It means: elements with same value are always in the same position
"""


def __default_comparer(a, b):
    return a < b


def mergesort(arr: list, compare_func: Callable = __default_comparer) -> None:
    """
    Performs mergesort sorting over the given array.

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
