import unittest
from scripts.extract_links import filter_external_links

class TestLinks(unittest.TestCase):

    def test_links_are_valid(self):
        xml_file = "tests/data/sample_links.xml"

        links = filter_external_links(xml_file)

        for link in links:
            self.assertTrue(
                link.startswith("http://") or link.startswith("https://"),
                f"Invalid URL detected: {link}"
            )