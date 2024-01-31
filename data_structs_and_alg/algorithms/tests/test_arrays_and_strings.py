import pytest

from data_structs_and_alg.algorithms.arrays_and_strings import (
    check_permutation,
    is_unique,
    is_unique_no_data_struct,
    one_way,
    palindrome_permutation,
    urlify,
)


@pytest.mark.parametrize(
    ['string', 'expected_answer'],
    [
        pytest.param(
            'ali',
            True,
            id='no duplicates',
        ),
        pytest.param(
            'alii',
            False,
            id='duplicates',
        ),
        pytest.param(
            'aaaali',
            False,
            id='duplicate at the beginning',
        ),
        pytest.param(
            'superr',
            False,
            id='duplicate at the beginning',
        ),
        pytest.param(
            '',
            True,
            id='empty string',
        ),
    ],
)
def test_is_unique(string, expected_answer):
    assert is_unique(string) == expected_answer


@pytest.mark.parametrize(
    ['string', 'expected_answer'],
    [
        pytest.param(
            'ali',
            True,
            id='no duplicates',
        ),
        pytest.param(
            'alii',
            False,
            id='duplicates',
        ),
        pytest.param(
            'aaaali',
            False,
            id='duplicate at the beginning',
        ),
        pytest.param(
            'superr',
            False,
            id='duplicate at the beginning',
        ),
        pytest.param(
            '',
            True,
            id='empty string',
        ),
    ],
)
def test_is_unique_no_data_struct(string, expected_answer):
    assert is_unique_no_data_struct(string) == expected_answer


@pytest.mark.parametrize(
    ['s1', 's2', 'expected_answer'],
    [
        pytest.param(
            'abcdef',
            'fedcba',
            True,
            id='is permutation',
        ),
        pytest.param(
            'ali',
            'lia',
            True,
            id='is permutation',
        ),
        pytest.param(
            '',
            '',
            True,
            id='empty strings',
        ),
        pytest.param(
            'abcdef',
            'fedcbag',
            False,
            id='is not permution',
        ),
        pytest.param(
            'abcdef',
            '',
            False,
            id='is not permutation - compare with empty string',
        ),
    ],
)
def test_check_permutation(s1, s2, expected_answer):
    assert check_permutation(s1, s2) == expected_answer


@pytest.mark.parametrize(
    ['s', 'expected_answer'],
    [
        pytest.param(
            'Mr John Smith    ',
            'Mr%20John%20Smith',
            id='trailing white space, two spaces to replace',
        ),
        pytest.param(
            'Mr   John Smith    ',
            'Mr%20%20%20John%20Smith',
            id='no trailing white space, four spaces to replace',
        ),
    ],
)
def test_urlify(s, expected_answer):
    assert urlify(s) == expected_answer


@pytest.mark.parametrize(
    ['s', 'expected_answer'],
    [
        pytest.param('tact coa', True, id='is palindrome perm'),
        pytest.param('ali', False, id='is not palindrome perm'),
        pytest.param(
            'civic',
            True,
        ),
        pytest.param(
            'aaaaaaaaa',
            True,
        ),
        pytest.param(
            ' civic',
            True,
        ),
    ],
)
def test_palindrome_permutation(s, expected_answer):
    assert palindrome_permutation(s) == expected_answer


@pytest.mark.parametrize(
    ['s1', 's2', 'expected_answer'],
    [
        pytest.param(
            'pale',
            'ple',
            True,
            id='one character removal',
        ),
        pytest.param(
            'pales',
            'pale',
            True,
            id='one character insertion',
        ),
        pytest.param(
            'pale',
            'bale',
            True,
            id='one character edit',
        ),
        pytest.param(
            'pale',
            'bake',
            False,
            id='two character edit',
        ),
        pytest.param(
            'pale',
            '',
            False,
            id='four character removal',
        ),
        pytest.param(
            'pale',
            'pall',
            True,
            id='edit at the end',
        ),
        pytest.param(
            'pale',
            'ppale',
            True,
            id='insert at the beginning',
        ),
    ],
)
def test_one_way(s1, s2, expected_answer):
    assert one_way(s1, s2) == expected_answer
