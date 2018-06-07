import unittest

def expect_exception(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""

    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)

        return test_decorated

    return test_decorator

def expect_exception1(exception):
    """Marks test to expect the specified exception. Call assertRaises internally"""

    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)

        return test_decorated

    return test_decorator


class MyTestCase(unittest.TestCase):
    @expect_exception(ValueError)
    @expect_exception1(ValueError)
    def test_value_error(self):
        int("A")  # test succeeds

    @expect_exception(ValueError)
    def test_value_error(self):
        int("0")  # test fails