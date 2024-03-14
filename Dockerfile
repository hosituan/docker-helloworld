FROM python:3.10.2
MAINTAINER Ho Si Tuan "hosituan.work@gmail.com"

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Update package manager cache and install tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
