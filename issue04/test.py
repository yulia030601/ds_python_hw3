import pytest
from one_hot_encoder import fit_transform


def test_one_hot_encode():
    continent = ['Europe', 'Latin America', 'Africa', 'Europe']
    exp = [
        ('Europe', [0, 0, 1]),
        ('Latin America', [0, 1, 0]),
        ('Africa', [1, 0, 0]),
        ('Europe', [0, 0, 1])
    ]
    assert fit_transform(continent) == exp


def test_only_two_genders():
    gender = ['male', 'female', 'male', 'male', 'male', 'female']
    for _ in fit_transform(gender):
        assert len(_[1]) == 2


def test_for_exception():
    with pytest.raises(Exception):
        fit_transform()


def test_for_only_element():
    el = ['Russia']
    exp = [('Russia', [1])]
    assert fit_transform(el) == exp
