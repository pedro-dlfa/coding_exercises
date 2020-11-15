import pytest
import random
from src.data_structures.queue_struct import Queue


def test_enqueue__multiple_elements__queue_order():
    queue_items = [i for i in range(random.randrange(10, 20))]
    sut = Queue()

    for i in queue_items:
        sut.enqueue(i)

    assert ", ".join(str(e) for e in queue_items) in str(sut)


def test_dequeue__multiple_elements__queue_order():
    queue_items = [i for i in range(random.randrange(10, 20))]
    sut = Queue()

    for i in queue_items:
        sut.enqueue(i)

    # dequeue some elements
    for i in range(random.randrange(2, 6)):
        expected_val = sut.dequeue()
        assert expected_val == queue_items.pop(0)

    assert ", ".join(str(e) for e in queue_items) in str(sut)


def test_dequeue__empty_queue__error():
    sut = Queue()

    with pytest.raises(IndexError):
        sut.dequeue()
