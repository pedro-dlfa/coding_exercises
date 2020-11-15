import os
import pytest
import pathlib
from src.exercises.pythagorean_triplet import Solution


testcases_files_path = os.path.join(
    pathlib.Path(__file__).parent, "test_pythagorean_triplet_cases"
)
testcases_no = int(len([name for name in os.listdir(testcases_files_path)]) / 2)


@pytest.mark.parametrize(
    "testfile_in,testfile_out",
    [
        (
            os.path.join(testcases_files_path, f"test_case_{i}_input.txt"),
            os.path.join(testcases_files_path, f"test_case_{i}_output.txt"),
        )
        for i in range(testcases_no)
    ],
)
def test_pythagorean_triplet__test_cases(testfile_in, testfile_out):

    with open(testfile_out) as tf_out:
        expected_result = tf_out.read()

    with open(testfile_in) as tf_in:
        n = int(tf_in.readline())
        arr = list(map(int, tf_in.readline().strip().split()))
        ans = Solution.check_triplet(arr)
        actual_result = "Yes" if ans else "No"
        assert actual_result == expected_result




