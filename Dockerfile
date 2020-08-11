FROM python:3

#   Utilizado para evitar problemas com usuaário root
RUN useradd -ms /bin/bash django && apt-get update && apt-get install python3-dev default-libmysqlclient-dev  -y && pip3 uninstall mysqlclient && pip3 uninstall pymysql &&  pip3 install mysqlclient
#   qualquer comando abaixo desse será executado
#   com usuário django
USER django

#   variavel utilizada para verificar valores
#   no terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app

#   utilizado para atualizar usuário
#   caso não seja atualizado pathway caso seja necessário
#   executar algum comando django ou python não irá fncionar

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/app

RUN pip install -r requirements.txt && pip3 install -U mysqlclient


#   copia tudo que tem na pasta do arquivo para conteiner
COPY . /home/django

