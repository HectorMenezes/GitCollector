FROM python:3.9
ENV PYTHONPATH=/APP
ENV PYTHONUNBUFFERED=TRUE
RUN mkdir /APP
WORKDIR /APP
COPY . .
RUN \
    apt-get update && \
    python -m pip install --upgrade pip && \
    pip install --default-timeout=200 future && \
    pip install -r requirements.txt && \
    apt-get install -y postgresql-client
# RUN \
#     curl -fsSL -o bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 && \
#     chmod +x bin/dbmate

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "/APP/entrypoint.sh"]
