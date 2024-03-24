import unittest

def foo(a,b):
    return a+b

class TestMyProgram(unittest.TestCase):
    def test_scrape_github_info(self):
        # Write test cases here
        self.assertEqual(foo(1,1), 2)
        # ""

if __name__ == '__main__':
    unittest.main()