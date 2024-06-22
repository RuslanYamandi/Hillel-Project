FROM python:3.12.2-slim

RUN apt update
RUN mkdir /shop

WORKDIR /shop

COPY ./src ./src
COPY ./run_server_dev.sh ./run_server_dev.sh
COPY ./requirements.txt ./requirements.txt

RUN python3 -m pip install --upgrade pip & pip install -r ./requirements.txt
RUN ["chmod", "+x", "./run_server_dev.sh"]

CMD ["bash"]

# sudo docker run --rm --name django_container -it -p 8050:8000 -v ./src:/shop/src shop