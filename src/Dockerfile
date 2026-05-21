FROM Python 3.10-slim
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "01_pipeline.py"]