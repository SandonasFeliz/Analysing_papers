import unittest
import os
from scripts.create_wordcloud import generate_wordcloud

class TestWordcloud(unittest.TestCase):

    def test_wordcloud_generation(self):

        text = "science science data science research science data data analysis analysis science machine machine machine machine learning science"

        output_folder = "tests"

        generate_wordcloud(text, output_folder, filename="test_wordcloud.png", show=False)

        self.assertTrue(os.path.exists("tests/test_wordcloud.png"))