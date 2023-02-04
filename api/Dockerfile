FROM python:3.10-buster
ENV PROJECT_ROOTDIR /app

WORKDIR ${PROJECT_ROOTDIR}

RUN apt-get update && apt-get install -y \
    curl \
    git

COPY ./api/requirements.txt ${PROJECT_ROOTDIR}/
COPY ./api ${PROJECT_ROOTDIR}/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN poetry install --no-dev


CMD ["python", "app.py"]