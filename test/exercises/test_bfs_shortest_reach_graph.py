import os
import pytest
import pathlib
from pytest_mock import mock
from src.exercises.bfs_shortest_reach_graph import Graph


testcases_files_path = os.path.join(
    pathlib.Path(__file__).parent, "test_bfs_shortest_reach_graph_cases"
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
def test_find_all_distances__test_cases(mocker, testfile_in, testfile_out):
    mock_print = mocker.patch("builtins.print")

    with open(testfile_in) as tf_in:
        tests_cnt = int(tf_in.readline())
        for i in range(tests_cnt):
            nodes, edges = [int(value) for value in tf_in.readline().split()]
            graph = Graph(nodes)
            for _ in range(edges):
                x, y = [int(x) for x in tf_in.readline().split()]
                graph.connect(x - 1, y - 1)
            s = int(tf_in.readline())
            graph.find_all_distances(s - 1)

    with open(testfile_out) as tf_out:
        print_calls = [mock.call(line) for line in tf_out.read().splitlines()]

    assert mock_print.mock_calls == print_calls
