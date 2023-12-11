# Flask Server with Threading
from flask import Flask, jsonify
import concurrent.futures
from scraper import scrape_cpu_info_from_urls, scrape_gpu_info_from_urls

app = Flask(__name__)

def scrape_with_threading(urls, scraper_function):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Scrape data concurrently using threads
        futures = {executor.submit(scraper_function, [url]): url for url in urls}  # Pass the URL as a list
        data = []
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                data.extend(result)
            except Exception as e:
                print(f"Failed to scrape data from {url}. Exception: {e}")
    return data


# URL to scrape CPU info
cpu_urls_to_scrape = [
    "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500",
    "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=24",
    "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=48",
]

@app.route('/cpu_info', methods=['GET'])  # GET route for CPU Info
def get_cpu_info():
    print("CPU URLs to scrape:", cpu_urls_to_scrape)  # Print or log the CPU URLs

    cpu_info = scrape_with_threading(cpu_urls_to_scrape, scrape_cpu_info_from_urls)
    return jsonify({'cpu_info': cpu_info})

# GPU's
gpu_urls_to_scrape = [
    "https://pricespy.co.uk/c/graphics-cards",
    "https://pricespy.co.uk/c/graphics-cards?offset=44",
]

@app.route("/gpu_info", methods=["GET"])
def get_gpu_info():
    print("GPU URLs to scrape:", gpu_urls_to_scrape)  # Print or log the GPU URLs
    gpu_info = scrape_with_threading(gpu_urls_to_scrape, scrape_gpu_info_from_urls)
    return jsonify({"gpu_info": gpu_info})

if __name__ == '__main__':
    app.run(debug=True)
