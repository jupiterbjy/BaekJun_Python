import unittest
import sys
from contextlib import contextmanager
from io import StringIO

from _2884 import func


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
        inputs = '10 10'
        expect = '9 25'

        with printCaptured() as (out, err):
            func(*inputs.split())

        output = out.getvalue().strip()
        self.assertEqual(str(expect), output)

    def testCase2(self):
        inputs = '0 30'
        expect = '23 45'

        with printCaptured() as (out, err):
            func(*inputs.split())

        output = out.getvalue().strip()
        self.assertEqual(str(expect), output)

    def testCase3(self):
        inputs = 23, 40
        expect = '22 55'

        with printCaptured() as (out, err):
            func(*inputs)

        output = out.getvalue().strip()
        self.assertEqual(str(expect), output)


if __name__ == '__main__':
    unittest.main()
