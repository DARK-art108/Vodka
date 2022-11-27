FROM python:3.7-slim-buster
RUN apt update -y && apt install awscli -y
COPY . /paraphraser
WORKDIR /paraphraser
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python","main.py" ]