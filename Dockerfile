FROM python:3.9
ENV PYTHONPATH=/APP
ENV PYTHONUNBUFFERED=TRUE
RUN mkdir /APP
WORKDIR /APP
COPY . .
RUN \
    apt-get update && \
    curl -fsSL -o /bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 && \
    chmod +x /bin/dbmate && \
    python -m pip install --upgrade pip && \
    pip install --default-timeout=400 future && \
    pip install -r requirements.txt && \
    apt-get install -y postgresql-client

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "/APP/entrypoint.sh"]
