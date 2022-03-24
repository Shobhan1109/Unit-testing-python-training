import unittest
def checkdiv(x):
    if x%7==0:
        return True
    else:
        return False
class check7app(unittest.TestCase):
    def test_case1(self):
        x=14
        r=checkdiv(x)
        self.assertTrue(r)

    def test_case2(self):
        x=13
        r=checkdiv(x)
        self.assertFalse(r)

if __name__=="__main__0":
    unittest.main()