# CostCompare
CostCompare is a full-stack application aimed at retrieving various computer hardware components information through created API endpoints using Web Scrapers. It enables users to compare prices of selected items and implements features like sorting for efficient data analysis.

## TechStack
- __Backend__: Python with Flask
- __Frontend__: ReactJS
- __Libraries/Tools__:
    - BeautifulSoup for bot automation
    - react-router-dom for frontend routes
    - MUI for icons
    - Bootstrap for various components

## Project Structure
The project has these key components
- __`scraper.py`__: Contains functions to scrape hardware components from specific URLs
- __`main.py`__: Flask app with API endpoints for hardware components
- Frontend React Components TBA

## Functionality
- __API Endpoints:__
    - __`/cpu_info`__: Contains info for CPUs
    - __`/gpu_info`__: Contains info for GPUs
    - __`/ram_info`__: Contains info for RAM
    - __`/psu_info`__: Contains info for Power Supplies
    - __`/cases_info`__: Contains info for Cases
 
## How to Run Project
- __Backend:__
    - Navigate to __`backend`__
    - Run __`pip install`__
    - Start server with __`python main.py`__

- __Frontend:__
    - Navigate to __`frontend`__
    - Run __`npm install`__
    - Start server with __`npm run dev`__

## Features table to implement:
- __Search Functionality:__
    - Add a search bar allowing users to quickly find hardware based on names
- __Pagination:__
    - Implement pagination for large lists of hardware to increase load time
- __Item Images:__
    - Include images with the items
- __Copy to Clipboard:__
    - Allow users to copy details of hardware
- __Error Handling:__
    - Display user-friendly error messages for failed API requests and data retrieval issues
- __Quick Compare Button:__
    - Enable a "Quick Compare" feature allowing users to compare two different items instantly
- __Third Party API's:__
    - Third party API integration for additional data or reviews on hardware
- __Price Comparison Chart:__
    - Implement visual representations (charts/graphs) to enchance price comparison
