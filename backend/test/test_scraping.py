# Unit test file for the scraper
# Run file with "python -m unittest test_scraping"

# Make sure terminal is in "test" folder
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(backend_dir)

import unittest
from scraper import scrape_cpu_info_from_url,scrape_gpu_info_from_url,scrape_psu_info_from_url,scrape_ram_info_from_url

class TestScrapingFunctions(unittest.TestCase):
    def test_cpu_scraping(self):
        cpu_data_url = "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500"
        cpu_data = scrape_cpu_info_from_url(cpu_data_url)
        self.assertIsNotNone(cpu_data)

        if cpu_data:
            for cpu in cpu_data:
                # Check if 'price' is a non-negative number
                self.assertIsInstance(cpu["price"], (int,float))
                self.assertGreaterEqual(cpu["price"], 0)

                # Check if 'name' and 'brand' are non-empty strings
                self.assertIsInstance(cpu['name'], str)
                self.assertIsInstance(cpu['brand'], str)
                self.assertNotEqual(cpu['name'], '')
                self.assertNotEqual(cpu['brand'], '')

                # Check if 'frequency' is either an empty string or a positive number
                if cpu['frequency'] != '':
                    self.assertIsInstance(cpu['frequency'], int)
                    self.assertGreater(cpu['frequency'], 0)
        
        print("CPU Test: 'test_cpu_scraping' Succeeded!")