import src.sorting.quicksort_algo as sut
import random


def test_quicksort__empty_array__no_error():
    original_input = []
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == []


def test_quicksort__one_element_array__no_error():
    original_input = [random.randrange(1000)]
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == original_input


def test_quicksort__random_multi_element_array__sorted():
    original_input = [random.randrange(1000) for _ in range(1000)]
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == sorted(original_input)


def test_quicksort__increasing_sorted_multi_element_array__sorted():
    original_input = sorted([random.randrange(1000) for _ in range(1000)])
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == original_input


def test_quicksort__decreasing_sorted_multi_element_array__sorted():
    original_input = sorted([random.randrange(1000) for _ in range(1000)], reverse=True)
    input_list = list(original_input)
    sut.quicksort(input_list)

    reversed_original_input = original_input[::-1]
    assert input_list == reversed_original_input


def test_quicksort__string_element_array__sorted(faker):
    original_input = [faker.pystr() for _ in range(1000)]
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == sorted(original_input)


def test_quicksort__float_element_array__sorted(faker):
    original_input = [random.random() for _ in range(1000)]
    input_list = list(original_input)
    sut.quicksort(input_list)
    assert input_list == sorted(original_input)


def test_quicksort__object_element_array__sorted(faker):
    class TestObject:
        """Test class to test object sorting

        Note: quicksort is unstable method. It means that it does not guarantee that two objects
        with same value always appear in the same order.
        Thus, the "__eq__" method implementation has been overwritten to solve this limitation
        in the test validation.
        """

        def __init__(self, value: int):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

        def __repr__(self):
            return f"Test({self.value})"

        def __str__(self):
            return f"<Test object - value: {self.value}>"

    original_input = [TestObject(random.randrange(1000)) for _ in range(1000)]
    input_list = list(original_input)
    sut.quicksort(input_list, lambda a, b: a.value < b.value)

    sorted_original_input = sorted(original_input, key=lambda e: e.value)
    assert input_list == sorted_original_input
