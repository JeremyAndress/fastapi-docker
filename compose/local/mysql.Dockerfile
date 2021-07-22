FROM mysql:8.0.26

ARG MYSQL_USER
ARG MYSQL_PASSWORD

CMD ["--default-authentication-plugin=mysql_native_password"]
