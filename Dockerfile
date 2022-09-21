FROM python:3.9-alpine

WORKDIR /apps
COPY main.py ./
RUN mkdir /data
RUN pip install fastapi uvicorn
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]
