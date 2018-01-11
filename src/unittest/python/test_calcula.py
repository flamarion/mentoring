import unittest
from src.main.python.calcula import Calcula


class TestSoma(unittest.TestCase):

    def setUp(self):
        pass

    def test_soma_2_2(self):
        x = Calcula(2, 2)
        self.assertTrue(x.soma() == 4)

    def teste_soma_3_3_fail(self):
        x = Calcula(3, 3)
        self.assertFalse(x.soma() == 5)


if __name__ == '__main__':
    unittest.main()