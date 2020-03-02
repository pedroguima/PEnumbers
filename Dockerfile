FROM alpine:3.10.3
RUN adduser -D pe && mkdir -p /usr/src/app && apk update && apk add git

ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

WORKDIR /usr/src/app
COPY src/ .
RUN pip3 install -r requirements.txt 
RUN chown -R pe /usr/src/app 

USER pe
EXPOSE 5000
CMD [ "python3", "api.py"]
