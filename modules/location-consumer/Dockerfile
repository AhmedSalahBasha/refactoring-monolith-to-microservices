FROM python:3.9-alpine

WORKDIR .

COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 6666

COPY . .
ENTRYPOINT ["python", "app/udaconnect/consumer.py"]