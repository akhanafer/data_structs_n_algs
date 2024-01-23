import os
from contextlib import nullcontext as does_not_raise

import pytest

from data_structs_and_alg.data_structures.arrays_and_strings.hash_table import HashTable

os.environ['PYTHONHASHSEED'] = '0'


@pytest.mark.parametrize(
    ['data', 'initial_size', 'expected_output', 'error'],
    [
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            5,
            '0 -> head -> (one,1) -> (two,2) -> (four,4) -> None\n'
            '1 -> head -> (three,3) -> (five,5) -> None\n'
            '2 -> head -> None\n'
            '3 -> head -> None\n'
            '4 -> head -> None\n',
            does_not_raise(),
            id='normal case',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            None,
            '0 -> head -> (two,2) -> (four,4) -> None\n'
            '1 -> head -> (five,5) -> None\n'
            '2 -> head -> None\n'
            '3 -> head -> None\n'
            '4 -> head -> None\n'
            '5 -> head -> (one,1) -> None\n'
            '6 -> head -> (three,3) -> None\n'
            '7 -> head -> None\n'
            '8 -> head -> None\n'
            '9 -> head -> None\n',
            does_not_raise(),
            id='no size',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            0,
            '',
            pytest.raises(ValueError),
            id='size 0',
        ),
    ],
)
def test_init(data, initial_size, expected_output, error):
    with error:
        ht = HashTable(*data, size=initial_size) if initial_size is not None else HashTable(*data)
        assert str(ht) == expected_output
        assert len(ht.table) == initial_size if initial_size else 10


@pytest.mark.parametrize(
    ['data', 'get_key', 'expected_output'],
    [
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            'five',
            5,
            id='normal case',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            '8',
            None,
            id='key does not exist',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            8,
            None,
            id='key of different type',
        ),
    ],
)
def test_get(data, get_key, expected_output):
    ht = HashTable(*data)
    res = ht.get(get_key)
    assert res == expected_output


@pytest.mark.parametrize(
    ['data', 'delete_key'],
    [
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            'five',
            id='normal case',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            'twenty',
            id='Key does not exist',
        ),
    ],
)
def test_delete(
    data,
    delete_key,
):
    ht = HashTable(*data)
    assert ht.delete(delete_key) is None
    assert ht.get(delete_key) is None


@pytest.mark.parametrize(
    ['data', 'insert_key', 'insert_value'],
    [
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            'six',
            6,
            id='normal case',
        ),
        pytest.param(
            [
                ['one', 1],
                ['two', 2],
                ['three', 3],
                ['four', 4],
                ['five', 5],
            ],
            'one',
            100,
            id='insert at existing key',
        ),
    ],
)
def test_insert(data, insert_key, insert_value):
    ht = HashTable(*data)
    assert ht.insert(insert_key, insert_value) is None
    assert ht.get(insert_key) == insert_value
    new_val = 10
    ht.insert(insert_key, new_val)
    assert ht.get(insert_key) == new_val
