from bs4 import BeautifulSoup
import re
import requests

# CPU Web Scraper
def scrape_cpu_info_from_urls(urls):
    cpu_info_list = []

    for url in urls:
        print("Scraping URL:", url)

        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find CPU names and prices
            cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]
            cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]

            # Extract relevant data for each CPU
            for name, price in zip(cpu_names, cpu_prices):
                name = name.get_text(strip=True)
                brand = name.split()[0] if name else ''  # Extracting the first word

                # Check if the brand is AMD or Intel
                if brand.lower() in ('amd', 'intel'):
                    cpu_info_list.append({
                        'name': name,
                        'brand': brand,
                        'price': price.get_text(strip=True)
                    })
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

    return cpu_info_list


# GPU Web Scraper
def scrape_gpu_info_from_urls(urls):
    gpu_info_list = []  # Initialize empty array to store info

    for url in urls:
        print("Scraping URL:", url)

        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")

            # Find GPU items
            gpu_items = soup.find_all('tr', class_='Tr-sc-1stvbsu-2 chMRiA')[:60]  # Limit to a length of 60

            # Extract relevant data for each GPU
            for item in gpu_items:
                full_name = item.find('h3', class_='ProductNameTable-sc-1stvbsu-3 bbvppQ').get_text(strip=True)
                price = item.find("span", class_="PriceLabel-sc-lboeq9-0").get_text(strip=True)
                extracted_price = re.search(r'£[\d,.]+', price)  # Removes any string except prices

                memory = ''
                gpu_properties = item.find_all('div', class_='PropertyContainer-sc-1stvbsu-11 TVmeo')
                for prop in gpu_properties:
                    if 'gb' in prop.get_text(strip=True).lower():
                        memory = prop.get_text(strip=True)
                        break

                if extracted_price:
                    brand = ''
                    name = full_name

                    # Extract GPU brand
                    if 'geforce' in full_name.lower() or 'radeon' in full_name.lower() or "intel" in full_name.lower():
                        if 'geforce' in full_name.lower():
                            brand = 'NVIDIA GeForce'
                        elif 'radeon' in full_name.lower():
                            brand = 'AMD Radeon'
                        elif 'intel' in full_name.lower():
                            brand = 'Intel ARC'

                    gpu_info_list.append({
                        'name': full_name,
                        'brand': brand,
                        'memory': memory,
                        'price': extracted_price.group()
                    })
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

    return gpu_info_list
