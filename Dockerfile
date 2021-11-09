FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.7/site-packages

COPY . .

CMD ["-f","/dev/null"]
