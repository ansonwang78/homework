FROM python:3.6-alpine
COPY ./app /app
WORKDIR /app
RUN pip install redis flask
CMD ["python","app.py"]
