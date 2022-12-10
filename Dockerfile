FROM python:3.10.9-slim-bullseye
RUN apt update
RUN apt install -y git curl apache2 apache2-dev libapache2-mod-wsgi-py3

# Install python dependencies
RUN mkdir /app
WORKDIR /app
COPY requeriments.txt /app
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

# Run permission script
COPY usuarios_permisos.py /app
RUN python usuarios_permisos.py

# Create a env
RUN virtualenv /plataforma_env
RUN /plataforma_env/bin/pip install -r requeriments.txt

