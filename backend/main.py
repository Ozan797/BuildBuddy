from flask import Flask, jsonify, request  # Import Flask framework for creating APIs and JSON response handling
from scraper import scrape_cpu_info_from_url, scrape_gpu_info_from_url,scrape_ram_info_from_url, scrape_psu_info_from_url  # Import functions to scrape CPU and GPU info
import concurrent.futures  # Import module for concurrent execution
from flask_cors import CORS

app = Flask(__name__)  # Create an instance of the Flask app
CORS(app)

@app.route('/cpu_info', methods=['GET'])  # Route to get CPU info
def get_cpu_info():
    search_query = request.args.get('search_query')  # Get the search query from the request URL

    # URLs to scrape CPU info
    cpu_urls_to_scrape = [
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=24",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=48",
    ]

    cpu_info = []  # List to store CPU info
    seen_cpus = set()  # Set to store seen CPU names to check for duplicates

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Scrape CPU info concurrently using ThreadPoolExecutor
        futures = [executor.submit(scrape_cpu_info_from_url, url) for url in cpu_urls_to_scrape]
        for future in concurrent.futures.as_completed(futures):
            info = future.result()  # Get the result of the completed task
            for cpu in info:
                if search_query is None or search_query.lower() in cpu['name'].lower():
                    # If no search query or CPU name contains the search query, add it to CPU info
                    if cpu['name'] not in seen_cpus:  # Check for duplicates
                        cpu_info.append(cpu)  # Add CPU info to the list
                        seen_cpus.add(cpu['name'])  # Add CPU name to the set of seen CPUs

    return jsonify({'cpu_info': cpu_info})  # Return JSON response with CPU info
@app.route('/amd_cpus', methods=['GET'])  # Route to get AMD CPUs only
def get_amd_cpus():
    cpu_urls_to_scrape = [
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=24",
        "https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500?offset=48",
    ]

    amd_cpus = []  # List to store AMD CPU info

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scrape_cpu_info_from_url, url) for url in cpu_urls_to_scrape]
        for future in concurrent.futures.as_completed(futures):
            info = future.result()
            for cpu in info:
                if cpu['brand'].lower() == 'amd':  # Check if the CPU brand is AMD
                    amd_cpus.append(cpu)

    return jsonify({'amd_cpus': amd_cpus})  # Return JSON response with AMD CPU info



@app.route("/gpu_info", methods=["GET"])  # Route to get GPU info
def get_gpu_info():
    # GPU URLs to scrape
    gpu_urls_to_scrape = [
        "https://pricespy.co.uk/c/graphics-cards",
        "https://pricespy.co.uk/c/graphics-cards?offset=44",
    ]
    
    gpu_info = []  # List to store GPU info
    seen_gpus = set()  # Set to store seen GPU names to check for duplicates

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Scrape GPU info concurrently using ThreadPoolExecutor
        futures = [executor.submit(scrape_gpu_info_from_url, url) for url in gpu_urls_to_scrape]
        for future in concurrent.futures.as_completed(futures):
            info = future.result()  # Get the result of the completed task
            for gpu in info:
                if gpu['name'] not in seen_gpus:  # Check for duplicates
                    gpu_info.append(gpu)  # Add GPU info to the list
                    seen_gpus.add(gpu['name'])  # Add GPU name to the set of seen GPUs

    return jsonify({"gpu_info": gpu_info})  # Return JSON response with GPU info

@app.route("/ram_info", methods=["GET"])  # Route to get GPU info
def get_ram_info():
    # GPU URLs to scrape
    ram_urls_to_scrape = [
        "https://pricespy.co.uk/c/ddr4-memory",
        "https://pricespy.co.uk/c/ddr4-memory?offset=44",
    ]
    
    ram_info = []  # List to store ram info
    seen_rams = set()  # Set to store seen ram names to check for duplicates

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Scrape ram info concurrently using ThreadPoolExecutor
        futures = [executor.submit(scrape_ram_info_from_url, url) for url in ram_urls_to_scrape]
        for future in concurrent.futures.as_completed(futures):
            info = future.result()  # Get the result of the completed task
            for ram in info:
                if ram['name'] not in seen_rams:  # Check for duplicates
                    ram_info.append(ram)  # Add ram info to the list
                    seen_rams.add(ram['name'])  # Add ram name to the set of seen rams

    return jsonify({"ram_info": ram_info})  # Return JSON response with ram info

@app.route("/psu_info", methods=["GET"])
def get_psu_info():
    psu_urls_to_scrape = [
        "https://pricespy.co.uk/c/power-supplies",
        "https://pricespy.co.uk/c/power-supplies?offset=44",
    ]
    
    psu_info = []  # List to store ram info
    seen_psu = set()  # Set to store seen ram names to check for duplicates

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Scrape ram info concurrently using ThreadPoolExecutor
        futures = [executor.submit(scrape_psu_info_from_url, url) for url in psu_urls_to_scrape]
        for future in concurrent.futures.as_completed(futures):
            info = future.result()  # Get the result of the completed task
            for ram in info:
                if ram['name'] not in seen_psu:  # Check for duplicates
                    psu_info.append(ram)  # Add ram info to the list
                    seen_psu.add(ram['name'])  # Add ram name to the set of seen rams

    return jsonify({"psu_info": psu_info})  # Return JSON response with ram info
    
if __name__ == '__main__':  # Run the Flask app if this script is executed directly
    app.run(debug=True)  # Start the Flask application with debugging enabled
