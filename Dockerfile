FROM python:3.9-slim

RUN apt update && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

