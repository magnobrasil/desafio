FROM ubuntu:latest

#  Instalando pacotes necessários
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apache2 curl lynx-cur wget openssl ssl-cert python-setuptools libapache2-mod-wsgi


# Liberando ssl
RUN a2enmod rewrite
RUN a2enmod ssl


#Definindo variaveis APACHE
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

#Definindo porta
EXPOSE 443

#Copiando index.html
COPY index.html /var/www/html/index.html

#Alterando conf do apache
ADD novo_apache.conf /etc/apache2/sites-enabled/000-default.conf

#Subindo Apache em primeiro plano
CMD /usr/sbin/apache2ctl -D FOREGROUND
