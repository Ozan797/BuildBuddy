from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

# Read the HTML content from the file
with open('website_content.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all CPU Names and limit to 24 items
cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]

# Find all CPU prices and limit to 24 items
cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]

# Ensure both CPU names and prices have the same length
if len(cpu_names) == len(cpu_prices):
    # Create a route to serve CPU information
    @app.route('/cpu_info', methods=['GET'])
    def get_cpu_info():
        cpu_info_list = []
        for name, price in zip(cpu_names, cpu_prices):
            cpu_info_list.append({
                'name': name.get_text(strip=True),
                'price': price.get_text(strip=True)
            })
        return jsonify({'cpu_info': cpu_info_list})

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
