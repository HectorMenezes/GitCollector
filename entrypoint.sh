#!/bin/bash
env
until  psql ${DATABASE_DSN} -c "\q"; do
  sleep 2
done

dbmate -e DATABASE_DSN up

uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload
