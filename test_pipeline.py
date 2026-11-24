import unittest
from main import run
class PipelineTest(unittest.TestCase):
    def test_demo(self):
        valid,issues=run()
        self.assertEqual(len(valid),2)
        self.assertEqual(len(issues),2)
        self.assertTrue(any('inconsistent' in x[2] for x in issues))
        self.assertTrue(any('nonnegative' in x[2] for x in issues))
if __name__=='__main__': unittest.main()
