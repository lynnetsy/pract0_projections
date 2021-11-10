FROM python:3.10
#FROM osgeo/proj

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

#RUN apk add --update --no-cache py3-numpy
#ENV PYTHONPATH=/usr/lib/python3.7/site-packages

COPY . .

CMD ["tail","-f","/dev/null"]

