from common import Common
import unittest

class TestCommonFunctions(unittest.TestCase):
    def setUp(self):
        self.common = Common()

    def test_permutations(self):
        # input = [1, 2]


        # output = self.common.permutations(input)


        # print "Sent in ", input, " got out ", output 

        # self.assertEqual(len(output), 3)
        # self.assertIn([1], output)
        # self.assertIn([2], output)
        # self.assertIn([1, 2], output)

        # -----

        input = [1, 2, 3]


        output = self.common.permutations(input)


        print "Sent in ", input, " got out ", output 

        self.assertEqual(len(output), 6)
        self.assertIn([1], output)
        self.assertIn([1, 2], output)
        self.assertIn([1, 2, 3], output)
        self.assertIn([2], output)
        self.assertIn([2, 3], output)
        self.assertIn([3], output)

if __name__ == '__main__':
    unittest.main()