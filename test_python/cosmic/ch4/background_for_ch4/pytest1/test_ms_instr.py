import unittest

class TestStuff(unittest):
    def test_inc(self):
        self.assertEqual(3,3)
    def test_dec(self):
        self.assertEqual(3,4)
if __name__=="__main__":
    unittest.main()
