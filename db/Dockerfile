FROM ubuntu:20.04

WORKDIR /home/db
COPY commands.txt /home/db/

RUN apt-get update
RUN apt-get install sqlite3 -y

ENTRYPOINT [ "sqlite3" ]
CMD ["pessoas.db commands.txt", ".quit"]
