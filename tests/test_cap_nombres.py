import unittest

def convert_names_to_caps(a):
    if len(a) > 10:
        raise ValueError('A maximum of 10 fish')
    return {"tank_a": a}


class TestConvertNamesToCaps(unittest.TestCase):
    def test_convert_names_to_caps_success(self):
        actual = convert_names_to_caps(a=["john", "pascal"])
        expected = {"a": ["john", "pascal"]}
        self.assertEqual(actual, expected)
