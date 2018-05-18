FROM alpine

RUN apk --update upgrade && apk add python3  python3-dev  gcc build-base
ADD . /

RUN pip3 install -r requirements.txt

CMD python3 main.py
