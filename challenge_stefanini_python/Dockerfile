FROM python:3.5
ENV PYTHONNUNBUFFERED 1

RUN mkdir /code
WORKDIR /code


ADD . /code/

RUN pip3 install -r requirements.txt && \ 
    chmod +x boot.sh

CMD ["./boot.sh"]

