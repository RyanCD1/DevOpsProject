FROM mysql:5.7
ENV MYSQL_INITDB_SKIP_TZINFO=1
ENV SECRET_KEY=test 
COPY ./Create.sql /docker-entrypoint-initdb.d
