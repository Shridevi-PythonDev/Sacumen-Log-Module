import unittest
import sac_log_module

class TestLog(unittest.TestCase):

    def test_errors(self):
        ecount = sac_log_module.errors_count(sac_log_module.read_log_file)
        self.assertEqual(ecount, 17155)
        #self.assertEqual(ecount, 17150)

    def test_warnings(self):
        wcount = sac_log_module.warnings_count(sac_log_module.read_log_file)
        self.assertEqual(wcount, 741)
        #self.assertEqual(wcount, 171)

    def test_info(self):
        icount = sac_log_module.info_count(sac_log_module.read_log_file)
        self.assertEqual(icount, 759)
        #self.assertEqual(icount, 27150)

    def test_total_log_count(self):
        lcount = sac_log_module.total_log_count(sac_log_module.read_log_file)
        self.assertEqual(lcount, 18703)
        #self.assertEqual(lcount, 1750)

    def test_get_file_size(self):
        size = sac_log_module.get_file_size(sac_log_module.read_log_file)
        self.assertEqual(size, 2.198)
        #self.assertEqual(size, 1.0) 
 
if __name__ == '__main__':
    unittest.main()
