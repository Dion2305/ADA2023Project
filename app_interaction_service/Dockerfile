# Using python 3.10 slim image as the base image
FROM python:3.10.7-slim
# Defining working directory and copy the requirements file
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Expose the port that this app runs on
EXPOSE 5003
# Set the environment variables
ENV DB_URL 'sqlite:///beers.db'
CMD ["python3","app.py"]