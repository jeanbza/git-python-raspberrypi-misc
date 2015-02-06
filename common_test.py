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

        input = [3,4,5,6,7]


        output = self.common.permutations(input)


        print "Sent in ", input, " got out ", output 

        # C(5,1)
        self.assertIn([3], output)
        self.assertIn([4], output)
        self.assertIn([5], output)
        self.assertIn([6], output)
        self.assertIn([7], output)

        # C(5,2)
        self.assertIn([3,4], output)
        self.assertIn([3,5], output)
        self.assertIn([3,6], output)
        self.assertIn([3,7], output)
        self.assertIn([4,5], output)
        self.assertIn([4,6], output)
        self.assertIn([4,7], output)
        self.assertIn([5,6], output)
        self.assertIn([5,7], output)
        self.assertIn([6,7], output)

        # C(5,3)
        self.assertIn([3,4,5], output)
        self.assertIn([3,4,6], output)
        self.assertIn([3,4,7], output)
        self.assertIn([3,5,6], output)
        self.assertIn([3,5,7], output)
        self.assertIn([3,6,7], output)
        self.assertIn([4,5,6], output)
        self.assertIn([4,5,7], output)
        self.assertIn([4,6,7], output)
        self.assertIn([5,6,7], output)

        # C(5,4)
        self.assertIn([3,4,5,6], output)
        self.assertIn([3,4,5,7], output)
        self.assertIn([3,5,6,7], output)
        self.assertIn([3,5,6,7], output)
        self.assertIn([4,5,6,7], output)

        # C(5,5)
        self.assertIn([3,4,5,6,7], output)

        self.assertEqual(len(output), 31)

if __name__ == '__main__':
    unittest.main()