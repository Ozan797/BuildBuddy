# Flask Server
from flask import Flask, jsonify
from scraper import scrape_cpu_info

app = Flask(__name__)

# Path to your HTML content
CPU_INFO_PG1 = 'cpu_info_pg1.html'
CPU_INFO_PG2 = 'cpu_info_pg2.html'

@app.route('/cpu_info', methods=['GET']) # GET route for CPU Info
def get_cpu_info():
    cpu_info_pg1 = scrape_cpu_info(CPU_INFO_PG1) # Runs function for that webpage
    cpu_info_pg2 = scrape_cpu_info(CPU_INFO_PG2) # Runs function for that webpage
    cpu_info = cpu_info_pg1 + cpu_info_pg2
    
    return jsonify({'cpu_info': cpu_info})

if __name__ == '__main__':
    app.run(debug=True)
