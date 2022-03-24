import unittest
def check(x):
    if x%2==0:
        return"even"
    else:
        return"odd"

class evenoroddapp(unittest.TestCase):
    def test_case_even(self):
        x=10
        r = check(x)
        self.assertEqual("even",r)

    def test_case_odd(self):
        x=11
        r = check(x)
        self.assertNotEqual("even",r)


if __name__=="__main__":
    unittest.main()