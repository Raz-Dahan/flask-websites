FROM python:3.8

# Set a directory for the app
WORKDIR /usr/src/app

# Copy all the files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Tell the port number the container should expose
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--port=5000", "--host=0.0.0.0"]
