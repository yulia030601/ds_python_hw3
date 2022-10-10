import unittest
from one_hot_encoder import fit_transform


class TestFitTranform(unittest.TestCase):
    def test_with_repeated_values(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
        self.assertEqual(actual, expected)

    def test_without_repeated_values(self):
        actual = fit_transform(['green', 'yellow', 'red'])
        expected = [
            ('green', [0, 0, 1]),
            ('yellow', [0, 1, 0]),
            ('red', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_not_iterable(self):
        wrong_input = 330
        with self.assertRaises(TypeError):
            fit_transform(wrong_input)

    def test_empty_string(self):
        with self.assertRaisesRegex(TypeError, 'expected at least 1 arguments, got 0'):
            fit_transform()





