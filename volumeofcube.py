import unittest

def checkvol(x):
    return x*x*x

class Checkvolcube(unittest.TestCase):
    def test_case1(self):
        x=5.555
        r=checkvol(x)
        self.assertAlmostEqual(r, x*x*x)

if __name__ == "__main__":
    unittest.main()