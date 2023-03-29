#Defines the base image it runes on
FROM httpd:latest
RUN apt-get update && \
    apt install apache2 -y && \ 
    apt-get install python3 python3-pip -y && \
    apt-get install vim -y && \
    apt-get install default-mysql-client -y && \
    apt-get install -y default-libmysqlclient-dev && \ 
    pip3 install mysqlclient && \
    rm /usr/local/apache2/htdocs/index.html 
COPY /apache/index.html /usr/local/apache2/htdocs
RUN cd conf && \
    echo "LoadModule cgid_module modules/mod_cgid.so" >> httpd.conf && \
    echo "ScriptAlias /cgi-bin/ /usr/local/apache2/cgi-bin/" >> httpd.conf
COPY /apache/db.py /usr/local/apache2/cgi-bin
RUN cd /usr/local/apache2/cgi-bin/ && \
    chmod a+x db.py
EXPOSE 80
