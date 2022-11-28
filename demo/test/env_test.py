import unittest
from . import TEST


class EnvTest(unittest.TestCase):

    def test_env(self):
        self.assertTrue(TEST, "test")
