FROM --platform=linux/amd64 python:3.12-alpine AS build

COPY . .

RUN pip install --upgrade pip
RUN pip install requests python-dotenv

RUN crontab crontab

CMD ["crond", "-f"]