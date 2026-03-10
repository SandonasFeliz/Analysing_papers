import unittest
import os

class TestPDF(unittest.TestCase):

    def test_file_is_pdf(self):
        file_path = "tests/data/paper_sample.pdf"

        self.assertTrue(os.path.exists(file_path))
        self.assertTrue(file_path.lower().endswith(".pdf"))
