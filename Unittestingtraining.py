import unittest
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

class myapp(unittest.TestCase):
    def test_case1(self):
        a=10
        b=20
        result = add(a,b)
        self.assertEqual(a+b, result)

    def test_csae2(self):
        a=10
        b=20
        result = sub(a,b)
        self.assertEqual(a-b, result)


if __name__=="__main__":
    unittest.main()
