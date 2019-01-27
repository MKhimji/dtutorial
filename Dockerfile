FROM python:3.6.6-alpine3.7

LABEL maintainer="Muhammad Khimji"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup -g 1000 -S m && adduser -u 1000 -S m -G m -s /usr/bin/fish m

WORKDIR /app
COPY . /app
 
RUN chown -R m /app
RUN chmod -R u+rX /app


RUN apk --no-cache add shadow \
                       build-base \
                       # dev dependencies
                       sudo \
		               git \
                       fish \
                       vim\
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev\
                       # psycopg2 dependencies
                       postgresql-dev\
                       postgresql-client


RUN pip install pipenv 
RUN pipenv install --deploy --system


USER m

EXPOSE 8000

CMD [ "fish", "funicorn_start" ] 












