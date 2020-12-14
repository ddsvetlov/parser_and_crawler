import unittest
import io
import os

class CrawlTest(unittest.TestCase):
	def test_pages(self):
		self.assertListEqual(list(io.open(os.getcwd()+"/test.txt")),
    					 list(io.open(os.getcwd()+"/TestPages/test_data.txt")))


if __name__ == '__main__':
  unittest.main()