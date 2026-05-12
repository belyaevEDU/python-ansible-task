FROM ubuntu:22.04@sha256:962f6cadeae0ea6284001009daa4cc9a8c37e75d1f5191cf0eb83fe565b63dd7

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y python3=3.10.6-1~22.04.1 python3-pip=22.0.2+dfsg-1ubuntu0.7 && rm -rf /var/lib/apt/lists

COPY ./python/requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY ./python .

CMD ["python3", "main.py"]