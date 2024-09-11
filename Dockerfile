# Use the official Streamlit image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code
COPY . .

# Set the Streamlit configuration (for running on a specific port)
ENV STREAMLIT_PORT=8503
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose the necessary port
EXPOSE 8503

# Command to run the Streamlit app
CMD ["streamlit", "run", "app/main.py", "--server.port=8503", "--server.address=0.0.0.0"]