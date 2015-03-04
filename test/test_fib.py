__author__ = 'nick'

import unittest

from fibonacci import fib


class TestFib(unittest.TestCase):

    def test_fib(self):
        seq = fib(5)
        self.assertIsNotNone(seq)
        self.assertIsInstance(seq, list)
        self.assertGreater(len(seq), 0)
        self.assertEquals(seq, [0, 1, 1, 2, 3])

    def fib_fail(self):
        return fib(-5)

    def test_fib_fail(self):
        self.assertRaises(Exception, self.fib_fail)
