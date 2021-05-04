import name
import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.name('Matthew', 'Gragg'),'Matthew Gragg')
    def test2(self):
        self.assertEqual(name.name('Billy', 'Bob'), 'Jane Doe')
    def test3(self):
        self.assertEqual(name.name('11 11', '-6.7'), '11 11 -6.7')
        
if __name__ == '__main__':
    unittest.main()