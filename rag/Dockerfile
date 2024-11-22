FROM python:3.11

WORKDIR /app
COPY rag/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python"]