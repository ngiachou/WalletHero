FROM python:latest

ADD . /test-products-api

WORKDIR /test-products-api

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# command for debugging
#CMD ["tail", "-f", "/dev/null"]