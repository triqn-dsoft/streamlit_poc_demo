# JIVF Credit Score AI Demo 

## Overview
This project is a web application that loads form input data, processes API calls for predictions, and displays charts based on the data. The application supports four product categories: Personal Loan (PL), Motorbike (MB), New Car (Car), and Truck, each with their respective form input data and configurations. 

The project uses Docker for containerization and includes helper files for CSS and input form management. Dummy JSON files are provided for research and development purposes.

## Project Structure

```bash
├── docker-compose.yml        # Docker Compose file to manage multi-container Docker applications
├── Dockerfile                # Dockerfile to build the Docker image for the app
├── requirements.txt          # Python dependencies
└── app
    ├── main.py               # Main program to load form input data, call API for predictions, and display charts
    ├── helper.py             # Helper class for common and individual product categories (PL, MB, Car, Truck)
    ├── css_helper.py         # CSS helper class for styling
    ├── json_collections/     # Folder containing dummy JSON files for each product category (PL, MB, Car, Truck)
    ├── demo_shap_chart.png     # Dummy chart data
    ├── header_1.png.png       # Image header cho đẹp
└── documents                 # Documentation and related files
## Overview
docker-compose up --build

## Configuration
Update variable BASE_URL (local IP address) and port in docker-compose.yml/environment
environment:
      - STREAMLIT_SERVER_PORT=8503
      - BASE_URL=http://192.168.4.255:8000/
## Overview