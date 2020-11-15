class Solution:
    """Find a pythagorean triplet in an array

    Given an array of integers, write a function that returns true if there is a triplet (a, b, c)
    that satisfies a^2 + b^2 = c^2.

    Find more details on: https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
    """

    @staticmethod
    def check_triplet(arr):
        # Sort array in descending order
        arr.sort(reverse=True)
        # Compute e^2 for all elements
        arr = [e * e for e in arr]

        # Take 'a' - largest element
        for idx_a in range(len(arr) - 3):
            idx_b = idx_a + 1
            idx_c = len(arr) - 1

            # The array is sorted, so the appropriate values of 'b' and 'c' will be found by:
            # - increasing 'idx_b' to try a smaller 'b'
            # - decreasing 'idx_c' to try a larger 'c'
            while idx_b < idx_c:
                a = arr[idx_a]
                b = arr[idx_b]
                c = arr[idx_c]

                if a > b + c:
                    # 'c' is too small, check next 'c'
                    idx_c -= 1
                elif a < b + c:
                    # 'b' is too large, check next 'b'
                    idx_b += 1
                else:
                    # Pythagorean triple found
                    return True

        return False
