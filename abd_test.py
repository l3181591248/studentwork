from ddt import ddt,data,unpack
import unittest
from abs import abs

@ddt
class Abs_test(unittest.TestCase):
    def setUp(self):
        print("abs_test star...")
    @data([-1,1], [1, 1], [0, 0])
    @unpack
    def test_abs(self,n,expect_value):
        result=abs(n)
        self.assertEqual(result,expect_value,msg=result)
    def tearDown(self):
        print("test end...")
if __name__=="__main__":
    unittest.main(verbosity=2)