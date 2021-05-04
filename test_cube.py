import unittest
import cube

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.cube_volume(4.5), 91.125)
    
    def test2(self):
        self.assertEqual(cube.cube_volume(-3), -27)
    
    def test3(self):
        self.assertEqual(cube.cube_volume('a'),0)

if __name__ == '__main__':
    unittest.main()