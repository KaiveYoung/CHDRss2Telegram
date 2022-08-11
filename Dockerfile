FROM python:3.10-slim as base
WORKDIR /app
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple

FROM base as builder
COPY ./app /app/app
COPY ./*.py /app/
RUN python3 -m compileall -b . \
    && mkdir  /tmp/builder  \
    && find . -name '*.pyc' -exec cp --parents \{\} /tmp/builder \;

FROM base
LABEL maintainer="Kaive Young <kaiveyoung@gmail.com>"
COPY --from=builder /tmp/builder /app
COPY ./instance /app/instance
EXPOSE 80