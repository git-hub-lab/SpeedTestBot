FROM python:3

WORKDIR /usr/src/app


COPY bot.py /usr/src/app/
COPY configs.py /usr/src/app
COPY speedtest.py /usr/src/app
COPY speedtestbot.py /usr/src/app

CMD [ "python", "./bot.py" ]
