__author__ = 'nick'

import unittest
import requests


class TestFibApi(unittest.TestCase):

    def test_fib(self):
        r = requests.get('http://localhost:8000/fib/5')
        self.assertEquals(r.status_code, 200)
        seq = r.json()
        self.assertIsNotNone(seq)
        self.assertIsInstance(seq, list)
        self.assertGreater(len(seq), 0)
        self.assertEquals(seq, [0, 1, 1, 2, 3])

    def test_fib_negative_fail(self):
        r = requests.get('http://localhost:8000/fib/-5')
        self.assertEquals(r.status_code, 400)

    def test_fib_nonnumeric_fail(self):
        r = requests.get('http://localhost:8000/fib/five')
        self.assertEquals(r.status_code, 400)

    def test_fib_post_fail(self):
        r = requests.post('http://localhost:8000/fib/5')
        self.assertEquals(r.status_code, 405)
