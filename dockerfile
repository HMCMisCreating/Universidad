FROM python:3.10.4-alpine

COPY . /appweb-gdc
WORKDIR /appweb-gdc

RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8000"]


