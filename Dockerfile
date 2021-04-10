FROM ubuntu
FROM python:3
ADD quizparse.py /
RUN pip install pystrich
COPY . .
ENTRYPOINT ["/sbin/tini", "--"]
CMD["python", "quizparse.py"]
