FROM python:3.11

WORKDIR /electronic_shop

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
