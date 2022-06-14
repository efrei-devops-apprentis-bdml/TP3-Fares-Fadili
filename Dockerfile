FROM python:alpine3.16

# set the working directory in the container
WORKDIR /Users/fares/Desktop/DevOps/TP1

COPY TP1.py ./


# install dependencies
RUN pip3 install --no-cache-dir -Iv requests===2.27.1
RUN pip3 install --no-cache-dir -Iv Flask===2.1.2

# command to run on container start
CMD [ "python3", "./TP1.py" ]

