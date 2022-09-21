#!/bin/bash
env
until  psql ${DB_CONNECTION_STRING} -c "\q"; do
  sleep 2
done

dbmate -e DATABASE_URL up

uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload
