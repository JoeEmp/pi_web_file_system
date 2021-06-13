from unittest import TestLoader, TextTestRunner, TestSuite
import os

if '__main__' == __name__:
    start_dir = os.path.abspath(os.path.dirname(__file__))
    suite = TestSuite()
    loader = TestLoader()
    all_cases = loader.discover(start_dir=start_dir, pattern='test_*.py')
    suite.addTests(all_cases)
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
