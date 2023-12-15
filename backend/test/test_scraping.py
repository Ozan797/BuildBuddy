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
                price = cpu["price"]
                self.assertIsInstance(cpu["price"], (float), f"CPU price '{price}' is not a float for CPU: {cpu['name']}")
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
        
    def test_gpu_scraping(self):
        gpu_data_url = "https://pricespy.co.uk/c/graphics-cards"
        gpu_data = scrape_gpu_info_from_url(gpu_data_url)
        self.assertIsNotNone(gpu_data)
        
        if gpu_data:
            for gpu in gpu_data:
                price = gpu["price"]
                # Make sure price is not negative and is a "int" or "float"
                self.assertIsInstance(gpu["price"], (float), f"GPU price '{price}' is not a float for GPU: {gpu['name']}")
                self.assertGreater(gpu["price"], 0)
                
                brands = {gpu['brand'] for gpu in gpu_data}  # Extract unique brands
                # Check if at least one of the expected brands is present in the scraped data
                expected_brands = {'NVIDIA GeForce', 'AMD Radeon', 'Intel ARC'}
                self.assertTrue(brands.intersection(expected_brands), "None of the expected brands found in the GPU data")

        print("GPU Test: 'test_gpu_scraping' Succeeded!")