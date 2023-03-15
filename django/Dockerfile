# FROM python:latest

# ENV DJANGODIR=/chat_app

# RUN mkdir -p $DJANGODIR
# WORKDIR $DJANGODIR

# COPY requirements.txt $DJANGODIR/
# RUN pip install -r requirements.txt

# COPY . $DJANGODIR/

# CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]

FROM python:latest

COPY django_chat_project/manage.py /

CMD ["python3", "manage.py", "runserver", "127.0.0.1:7000"]