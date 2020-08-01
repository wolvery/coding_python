FROM python:3-slim

WORKDIR /usr/app

RUN pip install pylint mypy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /usr/app

CMD ["python", "sample.py"]

