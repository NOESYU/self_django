FROM python:3.9.0

WORKDIR /home/

RUN echo "wefsdadsf"

RUN git clone https://github.com/NOESYU/self_django.git

WORKDIR /home/self_django/

#RUN echo "SECRET_KEY=django-insecure-c=4mpnnnhx!(prjc#_gy7am9acydk6gjtzf+p^da6kt+&s7q_b" > .env
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput --settings=selfdjango.settings.deploy && python manage.py migrate --settings=selfdjango.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=selfdjango.settings.deploy selfdjango.wsgi --bind 0.0.0.0:8000"]
