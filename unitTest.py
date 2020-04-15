import unittest
import sys
from contextlib import contextmanager
from io import StringIO

from _14681 import func


@contextmanager
def printCaptured():
    # https://stackoverflow.com/questions/4219717
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr

    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestBase(unittest.TestCase):

    def testCase1(self):
        inputs = 9, -13
        expect = 4

        with printCaptured() as (out, err):
            func(*inputs)

        output = out.getvalue().strip()
        self.assertEqual(str(expect), output)

    def testCase2(self):
        inputs = 12, 5
        expect = 1

        with printCaptured() as (out, err):
            func(*inputs)

        output = out.getvalue().strip()
        self.assertEqual(str(expect), output)


if __name__ == '__main__':
    unittest.main()
