import os
import pytest
import pathlib
import src.exercises.solve_coin as sut


testcases_files_path = os.path.join(
    pathlib.Path(__file__).parent, "test_solve_coin_cases"
)
testcases_no = int(len([name for name in os.listdir(testcases_files_path)]) / 2)


def test_solve_coin():
    denominations = [1, 2, 5]
    amount = 7
    result = sut.solve_coin_change(denominations, amount)

    for r in result:
        print(r)


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
def test_solve_coin__test_cases(testfile_in, testfile_out):
    with open(testfile_out) as tf_out:
        expected_result = [list(map(int, line.strip().split())) for line in tf_out]

    with open(testfile_in) as tf_in:
        amount = int(tf_in.readline())
        denominations = list(map(int, tf_in.readline().strip().split()))
        actual_result = sut.solve_coin_change(denominations, amount)

    expected_result = [sorted(lst) for lst in expected_result]
    expected_result.sort()
    actual_result = [sorted(lst) for lst in actual_result]
    actual_result.sort()

    assert expected_result == actual_result
