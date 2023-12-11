from bs4 import BeautifulSoup
import re

# CPU Web Scraper
def scrape_cpu_info(file_path):
    return _scrape_cpu_info_from_html(file_path)

def scrape_cpu_info_pg2(file_path):
    return _scrape_cpu_info_from_html(file_path)

def scrape_cpu_info_pg3(file_path):
    return _scrape_cpu_info_from_html(file_path)

def _scrape_cpu_info_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]
    cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]

    cpu_info_list = []
    for name, price in zip(cpu_names, cpu_prices):
        name = name.get_text(strip=True)
        brand = name.split()[0] if name else ''  # Extracting the first word

        # If the first word isn't AMD or Intel
        if brand.lower() in ('amd', 'intel'):  # Check if first word is AMD or Intel
            cpu_info_list.append({
                'name': name,
                'brand': brand,
                'price': price.get_text(strip=True)
            }) # Otherwise won't be added to the array

    return cpu_info_list


# GPU Web Scraper
def scrape_gpu_info(file_path):
    return _scrape_gpu_info_from_html(file_path)

def _scrape_gpu_info_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    gpu_items = soup.find_all('tr', class_='Tr-sc-1stvbsu-2 chMRiA')[:60]  # Limit to a length of 60
    gpu_info_list = [] # Initialise empty array to store info
    
    # For loop to parse through HTML Content
    for item in gpu_items:
        full_name = item.find('h3', class_='ProductNameTable-sc-1stvbsu-3 bbvppQ').get_text(strip=True)
        price = item.find("span", class_="PriceLabel-sc-lboeq9-0").get_text(strip=True)
        extracted_price = re.search(r'£[\d,.]+', price) # Removes any string excpet prices
        
        # Extracting GPU memory
        memory = ''
        gpu_properties = item.find_all('div', class_='PropertyContainer-sc-1stvbsu-11 TVmeo')
        for prop in gpu_properties:
            if 'gb' in prop.get_text(strip=True).lower(): # If "gb" is in string
                memory = prop.get_text(strip=True) # Save to memory variable
                break # Break loop
        
        if extracted_price:
            brand = '' # Empty brand string
            name = full_name  # Store the full name initially
            
            if 'geforce' in full_name.lower() or 'radeon' in full_name.lower() or "intel" in full_name.lower():
                # Extracting brand from the GPU name
                if 'geforce' in full_name.lower():
                    brand = 'NVIDIA GeForce'
                elif 'radeon' in full_name.lower():
                    brand = 'AMD Radeon'
                elif 'intel' in full_name.lower():
                    brand = 'Intel ARC'
                
            gpu_info_list.append({
                'name': full_name,  # Full name including brand
                'brand': brand,
                'memory': memory,
                'price': extracted_price.group()
            })
    
    return gpu_info_list