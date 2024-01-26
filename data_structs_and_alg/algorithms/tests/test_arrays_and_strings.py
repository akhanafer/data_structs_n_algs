import pytest

from data_structs_and_alg.algorithms.arrays_and_strings import (
    check_permutation,
    is_unique,
    is_unique_no_data_struct,
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
