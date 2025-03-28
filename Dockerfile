FROM cassandra:latest

WORKDIR /app

COPY data /data

EXPOSE 9042

CMD ["cassandra", "-f"]
