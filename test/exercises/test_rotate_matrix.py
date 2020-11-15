import os
import pytest
import pathlib
import src.exercises.rotate_matrix as sut


testcases_files_path = os.path.join(
    pathlib.Path(__file__).parent, "test_rotate_matrix_cases"
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
def test_rotate_matrix__test_cases(testfile_in, testfile_out):
    with open(testfile_out) as tf_out:
        expected_result = tf_out.read()

    with open(testfile_in) as tf_in:
        size = int(tf_in.readline())
        matrix_input = tf_in.readline().split()
        matrix = []
        for i in range(size):
            matrix.append(matrix_input[size * i : size * (i + 1)])

        sut.rotate_matrix(matrix, size)
        actual_result = sut.flatten_matrix(matrix, size)

        assert actual_result == expected_result
