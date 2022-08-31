FROM python:3.8

WORKDIR  /home/bot_pva

ADD . /home/bot_pva/

RUN pip install -r requirements.txt
RUN mkdir db
EXPOSE 5000/tcp

LABEL description='Teste de docker com um ubuntu, nginx e python tudo de uma vez'

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
