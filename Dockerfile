FROM python:3.9-alpine

COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install 'requests[socks]'

COPY ./app ./app

ENTRYPOINT [ "python", "-m", "app" ]
