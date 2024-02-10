FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY app.py .
COPY app_oficial.py .

#EXPOSE 5000
EXPOSE 8080

#CMD ["python", "app.py"]
CMD ["python", "app_oficial.py"]