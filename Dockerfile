FROM python:3.9-slim

RUN apt update && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt punkt_tab

CMD ["streamlit", "run", "app.py"]