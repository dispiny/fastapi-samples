FROM python:3.9-slim-buster
WORKDIR /apps/
COPY main.py .
RUN pip install fastapi uvicorn
EXPOSE 3000
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=3000"]