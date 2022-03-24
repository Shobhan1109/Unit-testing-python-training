import unittest

def logindata(username, password):
    if username=="admin" and password=="12345":
        return True
    else:
        return False

class loginapp(unittest.TestCase):
    def test_case1(self):
        r=logindata("admin","12345")
        self.assertEqual(r,logindata("admin","12345"))

    def test_case2(self):
        r = logindata("admin", "12365")
        self.assertNotEqual(r, logindata("admin", "12345"))

if __name__=="__main__":
    unittest.main()