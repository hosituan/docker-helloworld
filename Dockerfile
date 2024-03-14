FROM python:3.10.2
MAINTAINER Ho Si Tuan "hosituan.work@gmail.com"

# Set the working directory to /app
WORKDIR .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Update package manager cache and install tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr

# Run app.py when the container launches
CMD ["python", "app.py"]
