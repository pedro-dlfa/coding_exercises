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


def __partition(arr: list, low: int, high: int, compare_func: Callable = None) -> int:
    """
    Given an input array: selects the latest element as pivot, puts it in the expected sorted position
    and partitions the array on two unsorted chunks where the elements on the left
    chunk are smaller than the selected pivot and the elements on the right chunk are
    greater or equal than the selected pivot over the array chunk [low: high]

    :param arr: (list) Input array
    :param low: (int) Lower index
    :param high: (int) Higher index
    :param compare_func (Callable) Function to compare elements inside the array
    :return: (int) The partition index
    """
    if compare_func is None:
        compare_func = __default_comparer

    # Set pivot: latest element
    pivot = arr[high]
    # keep index to elements smaller than pivot
    smaller_idx = low - 1

    for i in range(low, high):
        # Swap at the left of the chunk the elements smaller than the pivot
        if compare_func(arr[i], pivot):
            smaller_idx += 1
            arr[smaller_idx], arr[i] = arr[i], arr[smaller_idx]

    # Swap the pivot at the correct position
    partition_idx = smaller_idx + 1
    arr[partition_idx], arr[high] = arr[high], arr[partition_idx]

    return partition_idx


def __quicksort(arr: list, low: int, high: int, compare_func: Callable) -> None:
    """
    Performs quicksort sorting over the chunk [low:high] of a given array.

    :param arr: (list) Input array
    :param low: (int) Lower index
    :param high: (int) Higher index
    :param compare_func (Callable) Function to compare elements inside the array
    """
    if low >= high:
        return

    # Perform partition and get partition index
    partition_idx = __partition(arr, low, high, compare_func)

    # Sort the partitions between the pivot
    __quicksort(arr, low, partition_idx - 1, compare_func)
    __quicksort(arr, partition_idx + 1, high, compare_func)


def quicksort(arr: list, compare_func: Callable = None) -> None:
    """
    Performs in-place quicksort sorting over the given array.

    :param arr: (list) Input array
    :param compare_func: (Callable) Function to compare elements inside the array
    """
    if len(arr) == 1:
        return

    __quicksort(arr, 0, len(arr) - 1, compare_func)
