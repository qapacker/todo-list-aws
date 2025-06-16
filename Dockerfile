FROM python:3.10-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl unzip git ca-certificates bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -Lo aws-sam-cli.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip && \
    unzip aws-sam-cli.zip -d sam-installation && \
    ./sam-installation/install && \
    rm -rf aws-sam-cli.zip sam-installation

WORKDIR /app

# 🧠 ESTA LÍNEA ES CLAVE
ENV PYTHONPATH="/app/src"

COPY . .

RUN pip install -r src/requirements.txt -t /app/src

RUN sam build

ENTRYPOINT []