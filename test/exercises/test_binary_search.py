import os
import pytest
import pathlib
import src.exercises.binary_search as sut


testcases_files_path = os.path.join(
    pathlib.Path(__file__).parent, "test_binary_search_cases"
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
def test_binary_search__test_cases(testfile_in, testfile_out):
    with open(testfile_in) as tf_in:
        k = int(tf_in.readline())
        arr = [int(x) for x in tf_in.readline().split()]
        actual_result = sut.binary_search(arr, k)

    with open(testfile_out) as tf_out:
        expected_result = tf_out.readline() == "True"

    assert expected_result == actual_result
