import random
from src.data_structures.bst_struct import Bst


def test_bst__empty__not_found():
    bst = Bst()
    assert not bst.search(random.randrange(1000))


def test_bst__insert__found():
    key = random.randrange(1000)

    bst = Bst()
    bst.insert(key)

    assert bst.search(key)


def test_bst__inorder__sorted():
    keys = []

    bst = Bst()
    for _ in range(random.randrange(20, 40)):
        key = random.randrange(1000)
        keys.append(key)
        bst.insert(key)

    assert bst.inorder() == sorted(keys)
