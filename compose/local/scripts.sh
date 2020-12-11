# TIME ZONE
apk add --update tzdata
# PACKAGE
apk update && apk add --no-cache gcc make \
    python3-dev
# DATABASE PACKAGE
if [ $MYSQL_SERVER ]
then
    echo "MYSQL DEPENDENCIES..."
    apk add --no-cache mariadb-dev build-base libffi-dev
fi