import pytest
import random
from src.data_structures.stack_struct import Stack


def test_push__multiple_elements__stack_order():
    queue_items = [i for i in range(random.randrange(10, 20))]
    sut = Stack()

    for i in queue_items:
        sut.push(i)

    assert ", ".join(str(e) for e in queue_items) in str(sut)


def test_pop__multiple_elements__stack_order():
    queue_items = [i for i in range(random.randrange(10, 20))]
    sut = Stack()

    for i in queue_items:
        sut.push(i)

    # dequeue some elements
    for i in range(random.randrange(2, 6)):
        expected_val = sut.pop()
        assert expected_val == queue_items.pop(-1)

    assert ", ".join(str(e) for e in queue_items) in str(sut)


def test_pop__empty_stack__error():
    sut = Stack()

    with pytest.raises(IndexError):
        sut.pop()
