from flask import Flask, jsonify
import concurrent.futures
from scraper import scrape_cpu_info_from_url, scrape_gpu_info_from_url

app = Flask(__name__)

@app.route("/", methods=["GET"])
def first_page():
    return "Welcome"

@app.route('/cpu_info', methods=['GET'])  # Route to get CPU info
def get_cpu_info():
    # URLs to scrape CPU info
    cpu_urls_to_scrape = [
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=24",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=48",
    ]

    cpu_info = []
    seen_cpus = set()  # To store seen CPU names to check for duplicates

    for url in cpu_urls_to_scrape:
        if url:  # Check if the URL is present
            info = scrape_cpu_info_from_url(url)
            # Check for duplicates before adding to cpu_info list
            for cpu in info:
                if cpu['name'] not in seen_cpus:
                    cpu_info.append(cpu)
                    seen_cpus.add(cpu['name'])

    return jsonify({'cpu_info': cpu_info})  # Return JSON of CPU info data for both URLs without duplicates


@app.route("/gpu_info", methods=["GET"])  # Route to get GPU info
def get_gpu_info():
    # GPU URLs to scrape
    gpu_urls_to_scrape = [
        "https://pricespy.co.uk/c/graphics-cards",
        "https://pricespy.co.uk/c/graphics-cards?offset=44",
    ]
    
    gpu_info = []
    seen_gpus = set()  # To store seen GPU names to check for duplicates

    for url in gpu_urls_to_scrape:
        if url:  # Check if the URL is present
            info = scrape_gpu_info_from_url(url)
            # Check for duplicates before adding to gpu_info list
            for gpu in info:
                if gpu['name'] not in seen_gpus:
                    gpu_info.append(gpu)
                    seen_gpus.add(gpu['name'])

    return jsonify({"gpu_info": gpu_info})  # Return JSON of GPU info data without duplicates

if __name__ == '__main__':
    app.run(debug=True)
