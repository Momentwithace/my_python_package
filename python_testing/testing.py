import unittest
from utils import add, square_list


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("I run only once")

    @classmethod
    def tearDownClass(cls) -> None:
        print("I run after all")

    # def test_for_error(self):
    #     with self.assertRaises(ValueError) as e:
    #         add("4", 2)
    #
    #     self.assertRaisesRegex(TypeError, "anything", add, "4", 2)

    def setUp(self) -> None:
        print("I run before each test case")

    def tearDown(self) -> None:
        print("I run after each test case")

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_list(self):
        self.assertListEqual([1, 4, 9], square_list([1, 2, 3]))

        """
        Given:

        When:

        Assert:

        """

if __name__ == '__main__':
    unittest.main()
