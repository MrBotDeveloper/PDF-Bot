FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils=0.71.* libcairo2=1.16.* libpango-1.0-0=1.42.* \
    libpangocairo-1.0-0=1.42.* libgdk-pixbuf2.0-0=2.38.* libffi-dev=3.2.* shared-mime-info=1.10-* ocrmypdf=8.0.* \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /bot
COPY . /bot
RUN pip install -r requirements.txt

RUN pybabel compile -D pdf_bot -d locale

EXPOSE ${PORT}

CMD ["python", "bot.py"]
