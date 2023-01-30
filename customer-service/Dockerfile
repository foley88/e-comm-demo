FROM python:3.10.9-slim-buster

WORKDIR /app

COPY requirements.txt ./


RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt


COPY . /src
COPY . /database
COPY . /routers


CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
