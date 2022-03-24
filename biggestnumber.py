import unittest

def biggnum(x,y):
    if(x>y):
        return "first"
    else:
        return "second"

class biggestnumber(unittest.TestCase):
    def test_case1(self):
        x=10
        y=5
        r=biggnum(x,y)
        self.assertEqual("first",r)

    def test_case2(self):
        x = 5
        y = 10
        r = biggnum(x, y)
        self.assertEqual("second", r)

if __name__=="__main__":
    unittest.main()