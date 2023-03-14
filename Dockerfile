FROM python:latest

COPY /chat_project/django_chat_project/manage.py /

CMD ["python", "./manage.py"]