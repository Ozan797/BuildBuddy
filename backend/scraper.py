from bs4 import BeautifulSoup

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

def scrape_gpu_info(file_path):
    return _scrape_gpu_info_from_html(file_path)

def _scrape_gpu_info_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    gpu_names = soup.find_all('h3', class_='ProductNameTable-sc-1stvbsu-3 bbvppQ')
    
    gpu_info_list = []
    
    for name in gpu_names:
        gpu_info_list.append({
            'name': name.get_text(strip=True)
        })
    
    return gpu_info_list
    

