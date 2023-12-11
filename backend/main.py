from flask import Flask, jsonify
import concurrent.futures
from scraper import scrape_cpu_info_from_urls, scrape_gpu_info_from_urls

app = Flask(__name__)

# Function to scrape data using threading
def scrape_with_threading(urls, scraper_function):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(scraper_function, [url]): url for url in urls}
        data = []
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                data.extend(result)
            except Exception as e:
                print(f"Failed to scrape data from {url}. Exception: {e}")
    return data

# URLs to scrape CPU info

@app.route('/cpu_info', methods=['GET'])  # Route to get CPU info
def get_cpu_info():
    cpu_urls_to_scrape = [
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=24",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=48",
        
        ]   
    cpu_info = scrape_cpu_info_from_urls(cpu_urls_to_scrape)
    return jsonify({'cpu_info': cpu_info})

@app.route("/gpu_info", methods=["GET"])  # Route to get GPU info
def get_gpu_info():
    gpu_urls_to_scrape = [
        "https://pricespy.co.uk/c/graphics-cards",
        "https://pricespy.co.uk/c/graphics-cards?offset=44",
    ]
    gpu_info = scrape_gpu_info_from_urls(gpu_urls_to_scrape)
    return jsonify({"gpu_info": gpu_info})

if __name__ == '__main__':
    app.run(debug=True)
