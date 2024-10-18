import unittest
from algorithms import bubble_sort

class Tests(unittest.TestCase):
    def test(self):
        print("Tests Ready")

    def test_bubble_sort_mixed(self):
        return
        list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
        output = bubble_sort(list)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(output, expected)


    def test_bubble_sort_reversed(self):
        return
        list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        output = bubble_sort(list)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(output, expected)


    def test_bubble_sort_sorted(self):
        return
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        output = bubble_sort(list)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(output, expected)



if __name__ == "__main__":
    unittest.main()
