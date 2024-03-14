FROM python:3.12.2
MAINTAINER Ho Si Tuan "hosituan.work@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get install tesseract-ocr
ENTRYPOINT ["python"]
CMD ["app.py"]
