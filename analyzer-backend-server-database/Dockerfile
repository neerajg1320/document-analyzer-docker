FROM neeraj76/poppler-pandas

RUN apt update

COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

COPY ./api-server/app /app
COPY ./api-server/database /database

COPY ./command.sh ./

CMD ["/bin/bash", "command.sh"]