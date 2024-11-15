FROM python:3.10

WORKDIR /root/Tanjiro

COPY ..

RUN pip install -r requirements.txt

CMD ["python3", "-m", "Tanjiro"]
