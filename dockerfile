FROM ubuntu:18.04

LABEL maintainer="dlatlrrb@gmail.com"

ENV KEY a3a7c3343f9df2af23b0670af1c8f38b823de2aca940f6417da15c6fd63be9cc

#If you want to test quickly, use this file
ENV HASH_FILE_NAME quick_hash_input.txt

#Default input file
# ENV HASH_FILE_NAME sample_hash_input.txt

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

RUN python3 virustotal-search.py -k ${KEY} -i ${HASH_FILE_NAME}

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]