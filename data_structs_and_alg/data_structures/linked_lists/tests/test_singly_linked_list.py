from contextlib import nullcontext as does_not_raise

import pytest
from data_structures.linked_lists.singly_linked_list import SinglyLinkedList


@pytest.mark.parametrize(
    ['data', 'expected_output', 'expected_size', 'expected_head', 'expected_tail'],
    [
        pytest.param(
            [1, 2, 3],
            'head -> 1 -> 2 -> 3 -> None',
            3,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(3),
            id='normal case',
        ),
        pytest.param(
            [None],
            'head -> None -> None',
            1,
            SinglyLinkedList.Node(None),
            SinglyLinkedList.Node(None),
            id='First item null',
        ),
        pytest.param(
            [[1, 2, 3]],
            'head -> [1, 2, 3] -> None',
            1,
            SinglyLinkedList.Node([1, 2, 3]),
            SinglyLinkedList.Node([1, 2, 3]),
            id='First item list',
        ),
        pytest.param(None, 'head -> None', 0, None, None, id='Empty List'),
    ],
)
def test_init(data, expected_output, expected_size, expected_head, expected_tail):
    if data:
        sll = SinglyLinkedList(*data)
    else:
        sll = SinglyLinkedList()

    assert str(sll) == expected_output
    assert sll.size == expected_size
    assert sll.head == expected_head
    assert sll.tail == expected_tail


@pytest.mark.parametrize(
    [
        'initial_data',
        'insert',
        'expected_output',
        'expected_size',
        'expected_head',
        'expected_tail',
    ],
    [
        pytest.param(
            [1, 2, 3],
            [4, 5, 6, 7],
            'head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None',
            7,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(7),
            id='list initialized with data',
        ),
        pytest.param(
            None,
            [1, 2, 3],
            'head -> 1 -> 2 -> 3 -> None',
            3,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(3),
            id='list initialized empty',
        ),
    ],
)
def test_insert(initial_data, insert, expected_output, expected_size, expected_head, expected_tail):
    if initial_data:
        sll = SinglyLinkedList(*initial_data)
    else:
        sll = SinglyLinkedList()

    for val in insert:
        sll.insert(val)
    assert str(sll) == expected_output
    assert sll.size == expected_size
    assert sll.head == expected_head
    assert sll.tail == expected_tail


@pytest.mark.parametrize(
    [
        'initial_data',
        'insert_data',
        'index',
        'expected_output',
        'expected_size',
        'expected_head',
        'expected_tail',
        'error',
    ],
    [
        pytest.param(
            [1, 2, 3],
            6,
            2,
            'head -> 1 -> 2 -> 3 -> 6 -> None',
            4,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(6),
            does_not_raise(),
            id='value added at the end',
        ),
        pytest.param(
            [1, 2, 3],
            6,
            0,
            'head -> 6 -> 1 -> 2 -> 3 -> None',
            4,
            SinglyLinkedList.Node(6),
            SinglyLinkedList.Node(3),
            does_not_raise(),
            id='value added at the beginning',
        ),
        pytest.param(
            None,
            6,
            0,
            'head -> 6 -> None',
            1,
            SinglyLinkedList.Node(6),
            SinglyLinkedList.Node(6),
            does_not_raise(),
            id='List initialized empty',
        ),
        pytest.param(
            [1, 2, 3],
            6,
            4,
            '',
            0,
            None,
            None,
            pytest.raises(IndexError),
            id='index out of range',
        ),
    ],
)
def test_insert_at(
    initial_data,
    insert_data,
    index,
    expected_output,
    expected_size,
    expected_head,
    expected_tail,
    error,
):
    with error:
        if initial_data:
            sll = SinglyLinkedList(*initial_data)
        else:
            sll = SinglyLinkedList()

        sll.insert_at(insert_data, index)
        assert str(sll) == expected_output
        assert sll.size == expected_size
        assert sll.head == expected_head
        assert sll.tail == expected_tail


@pytest.mark.parametrize(
    [
        'initial_data',
        'delete_at',
        'expected_output',
        'expected_size',
        'expected_head',
        'expected_tail',
        'error',
    ],
    [
        pytest.param(
            [1, 2, 3],
            1,
            'head -> 1 -> 3 -> None',
            2,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(3),
            does_not_raise(),
            id='list initialized with data',
        ),
        pytest.param(
            [1, 2, 3],
            2,
            'head -> 1 -> 2 -> None',
            2,
            SinglyLinkedList.Node(1),
            SinglyLinkedList.Node(3),
            does_not_raise(),
            id='delete last',
        ),
        pytest.param(
            [1, 2, 3],
            0,
            'head -> 2 -> 3 -> None',
            2,
            SinglyLinkedList.Node(2),
            SinglyLinkedList.Node(3),
            does_not_raise(),
            id='delete first',
        ),
        pytest.param(
            None,
            2,
            '',
            0,
            None,
            None,
            pytest.raises(IndexError),
            id='list initialized empty',
        ),
    ],
)
def test_delete(
    initial_data,
    delete_at,
    expected_output,
    expected_size,
    expected_head,
    expected_tail,
    error,
):
    with error:
        if initial_data:
            sll = SinglyLinkedList(*initial_data)
        else:
            sll = SinglyLinkedList()
        sll.delete(delete_at)
        assert str(sll) == expected_output
        assert sll.size == expected_size
        assert sll.head == expected_head
        assert sll.tail == expected_tail


@pytest.mark.parametrize(
    ['initial_data', 'get_index', 'expected_output', 'error'],
    [
        pytest.param([1, 2, 3], 1, 2, does_not_raise(), id='list initialized with data'),
        pytest.param([1, 2, 3], 0, 1, does_not_raise(), id='get first'),
        pytest.param([1, 2, 3], 2, 3, does_not_raise(), id='get last'),
        pytest.param(None, 2, 0, pytest.raises(IndexError), id='list initialized empty'),
    ],
)
def test_get(initial_data, get_index, expected_output, error):
    with error:
        if initial_data:
            sll = SinglyLinkedList(*initial_data)
        else:
            sll = SinglyLinkedList()
        assert sll.get(get_index) == expected_output
