FROM python:3.9-alpine

ADD ./tg_news /tg_news
WORKDIR /tg_news
RUN python -m venv venv && . ./venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]