import unittest
from tsp import *


class TestTSP(unittest.TestCase):
    def test_create_base_case(self):
        test_nodes = [i for i in range(5)]
        print(create_base_case(test_nodes))
        tsp(test_nodes)
        self.assertTrue(True)
        pass

if __name__ == "__main__":
    unittest.main()