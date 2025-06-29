FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
EXPOSE 8888

# Default to Streamlit (or remove this line to require explicit CMD)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]