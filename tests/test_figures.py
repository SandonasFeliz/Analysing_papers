import unittest
from scripts.figures_count import count_figures

class TestFigures(unittest.TestCase):

    def test_count_figures(self):
        print("Checking figure counting...")
        
        xml_file = "tests/data/sample_figures.xml"

        result = count_figures(xml_file)

        self.assertEqual(result, 2)