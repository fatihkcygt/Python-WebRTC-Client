FROM python:3-alpine
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev curl openssl-dev libxslt-dev netcat-openbsd

ADD requirements.pip /.
RUN pip install -r /requirements.pip

ADD entrypoint.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]

WORKDIR /code

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

