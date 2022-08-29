FROM ubuntu:20.04

WORKDIR  /home/bot_pva

ADD . /home/bot_pva/

# ENV $PATH = /home/bot_pva

RUN apt-get update 
# RUN apt-get install -y nginx 
RUN apt-get install -y net-tools 
# RUN apt-get install vim -y
RUN apt-get install nano -y
# RUN apt-get install gunicorn -y
# RUN apt-get install sqlite3 -y
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN pip install flask 
RUN pip install gunicorn
# RUN pip install pydantic 
# RUN pip install flask_pydantic_spec


LABEL description='Teste de docker com um ubuntu, nginx e python tudo de uma vez'

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
