FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir requests

WORKDIR /app
RUN useradd -m worker && chown worker:worker /app

COPY --chown=worker:worker requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY --chown=worker:worker http_script.py .

USER worker

CMD ["python3", "http_script.py"]
