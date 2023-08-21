This project is for receiving news from 4 sources via Telegram:

- rambler.ru
- lenta.ru
- iXBT.ru
- rbc.ru

You should fill 

[TOKEN]

API_TOKEN =

ADMIN_ID = 

in settings.ini. API_TOKEN might be received through Telegram's BotFather, ADMIN_ID is your own ID. You can send a message to all the subscribers by /sendall prefix, but it is is allowed only if you are ADMIN. For example:

/sendall Hi everyone!

A database is creating after first launch. It keeps all your subscribers and their statuses

Launching is easy: python ./main.py

If you want to launch the app as a container, put the Dockerfile on the same directory as tg_news directory and launch
- docker build -t tg_news .
- docker run tg_news