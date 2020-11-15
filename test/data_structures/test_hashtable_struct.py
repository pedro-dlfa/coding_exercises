import itertools
import string
from pytest_mock import mock

import pytest
import random
import src.data_structures.hashtable_struct as hashtable_struct
from src.data_structures.hashtable_struct import HashTable


def test_add__non_existing_element__inserted(faker):
    sut = HashTable()
    in_key = random.randrange(1000)
    in_value = faker.pystr()

    assert in_key not in sut
    sut.add(in_key, in_value)

    out_value = sut.get(in_key)
    assert in_value == out_value


def test_add__existing_element__updated(faker):
    sut = HashTable()
    in_key = random.randrange(1000)
    insert_value = faker.pystr()

    sut.add(in_key, insert_value)
    assert in_key in sut

    update_value = faker.pystr()
    sut.add(in_key, update_value)

    out_value = sut.get(in_key)
    assert update_value == out_value


def test_add_get__brackets_syntax__ok(faker):
    sut = HashTable()
    in_key = random.randrange(1000)
    in_value = faker.pystr()

    sut[in_key] = in_value

    out_value = sut[in_key]
    assert in_value == out_value


def test_get__non_existing_element_no_default_provided__none_returned(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    out_value = sut.get(in_key)

    assert out_value is None


def test_get__non_existing_element_default_provided__default_returned(
    faker,
):
    sut = HashTable()
    in_key = random.randrange(1000)
    expected_out = faker.pystr()

    actual_out = sut.get(in_key, default_value=expected_out)

    assert actual_out is expected_out


def test_get__non_existing_element_brackets_syntax__key_error(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    with pytest.raises(KeyError) as actual_error:
        sut[in_key]

    assert str(actual_error.value) == str(in_key)


def test_contains__check_existing_element__true(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    sut.add(in_key, None)
    actual_out = in_key in sut

    assert actual_out == True


def test_contains__check_non_existing_element__false(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    actual_out = in_key in sut

    assert actual_out == False


def test_remove__non_existing_element__key_error(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    with pytest.raises(KeyError) as actual_error:
        sut.remove(in_key)

    assert str(actual_error.value) == str(in_key)


def test_remove__existing_element__ok(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    sut.add(in_key, None)
    assert in_key in sut

    sut.remove(in_key)
    actual_out = in_key in sut

    assert actual_out == False


def test_remove__non_existing_element_del_syntax__key_error(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    with pytest.raises(KeyError) as actual_error:
        del sut[in_key]

    assert str(actual_error.value) == str(in_key)


def test_remove__existing_element_del_syntax__ok(faker):
    sut = HashTable()
    in_key = random.randrange(1000)

    sut[in_key] = None
    assert in_key in sut

    del sut[in_key]
    actual_out = in_key in sut

    assert actual_out == False


def test_add__collisioning_elements__ok(faker):
    initial_size = 10
    # Build random string whose hash could match in the hashtable
    keys = [
        "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        for _ in range(10000)
    ]
    group_keys_by_hash = itertools.groupby(keys, key=lambda e: hash(e) % initial_size)
    # Select the group of values with more collisions
    max_group = max(
        ((k, list(g)) for k, g in group_keys_by_hash), key=lambda g: len(g[1])
    )

    if len(max_group[1]) < 2:
        pytest.skip("No duplicated hash found. Skipping...")

    sut = HashTable(initial_size)
    key1 = max_group[1][0]
    key2 = max_group[1][1]
    exp_val1 = str(key1)
    exp_val2 = str(key2)

    # Add two keys with expected same hash cell
    sut.add(key1, exp_val1)
    sut.add(key2, exp_val2)
    out_key1 = sut.get(key1)
    out_key2 = sut.get(key2)

    assert key1 != key2
    assert out_key1 == exp_val1
    assert out_key2 == exp_val2


def test_add__resize__ok(faker, mocker):
    initial_size = 10
    keys = [
        "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        for _ in range(random.randrange(200, 1000))
    ]
    log_mock = mocker.patch.object(hashtable_struct.log, "debug")

    # check number of increase operations
    fill_factor = 2 / 3
    resize_ops = 0
    while initial_size * pow(2, resize_ops) * fill_factor < len(keys):
        resize_ops += 1

    # Insert all elements
    sut = HashTable(initial_size)
    for k in keys:
        sut.add(k, str(k))

    # Validate all elements in HashTable
    for k in keys:
        val = sut[k]
        assert val == str(k)

    expected_calls = []
    for i in range(1, resize_ops + 1):
        expected_calls.append(mock.call("HashTable is pretty filled. Resizing..."))
        expected_calls.append(
            mock.call(f"New HashTable size is: {initial_size * pow(2, i)}")
        )

    assert log_mock.mock_calls == expected_calls
