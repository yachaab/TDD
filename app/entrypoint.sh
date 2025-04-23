#!/bin/sh

# Define color codes
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
RESET="\033[0m"

if [ "$DATABASE" = "postgres" ]
then
    echo -e "${YELLOW}Waiting for postgres...${RESET}"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      echo -e "${YELLOW}Connecting to Postgres, please wait a second...${RESET}"
      sleep 0.1
    done

    echo -e "${GREEN}PostgreSQL is connected ${RESET}"
fi

echo -e "${YELLOW}Creating database tables...${RESET}"
python manage.py flush --no-input
python manage.py migrate
echo -e "${GREEN}Database tables created${RESET}"

exec "$@"