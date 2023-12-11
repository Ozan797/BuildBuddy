# Flask Server
from flask import Flask, jsonify
from scraper import scrape_cpu_info_from_url, scrape_gpu_info

app = Flask(__name__)

# URL to scrape CPU info
CPU_INFO_URL = 'https://pricespy.co.uk/computers-accessories/computer-components/cpus--c500'

@app.route('/cpu_info', methods=['GET'])  # GET route for CPU Info
def get_cpu_info():
    cpu_info = scrape_cpu_info_from_url(CPU_INFO_URL)  # Scrape CPU info from URL
    
    return jsonify({'cpu_info': cpu_info})
# GPU's
gpu_info_pg1_path = "gpu_info_pg1.html"

@app.route("/gpu_info", methods=["GET"])
def get_gpu_info():
    gpu_info = scrape_gpu_info(gpu_info_pg1_path)
    
    return jsonify({"gpu_info": gpu_info})

if __name__ == '__main__':
    app.run(debug=True)
