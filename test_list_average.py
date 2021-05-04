import unittest
import list_average

test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list2 = []
test_list3 = [1,-1, 2, -10, 8, 11, -12, 1, 100, -99, -1]
class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(list_average.average(test_list1), 5.5)
    
    def test2(self):
        self.assertEqual(list_average.average(test_list2), 1)
    
    def test3(self):
        self.assertEqual(list_average.average(test_list3), 0)

if __name__ == '__main__':
    unittest.main()