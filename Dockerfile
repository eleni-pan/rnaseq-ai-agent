FROM python:3.12-slim

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y build-essential gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ /app/data/
COPY scripts/ /app/scripts/
COPY utils/ /app/utils/

CMD ["tail", "-f", "/dev/null"]
