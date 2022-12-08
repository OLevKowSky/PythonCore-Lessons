import unittest
from src.add.adding import adding

x = 2
y = 2


def test_add(x, y):
    assertEqual(adding(x, y), 4)


unittest.main()
