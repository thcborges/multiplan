FROM python:3.10 as base
ARG UNAME=app
ARG UID=1000
ARG GID=1000

# Update repositories
RUN apt update && apt upgrade -y && apt autoremove -y
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV HOME=/home/$UNAME

# Create user
RUN groupadd -g $GID app && useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
RUN chown -R $UNAME $HOME
USER $UNAME


FROM base as development

ARG UNAME=app
ARG UID=1000
ARG GID=1000
# Install wget to download poetry
USER root
RUN apt install -y curl


RUN mkdir -p $HOME/app
WORKDIR $HOME/app

# Install poetry
ENV POETRY_VERSION=1.4.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$HOME/.local/bin:$PATH

# Build project
COPY ./poetry.lock ./pyproject.toml ./README.md ./
COPY ./multiplan ./multiplan
COPY ./data/renttherunway_final_data.json ./data/renttherunway_final_data.json

RUN poetry install 
RUN python multiplan/build.py
RUN chown -R $UNAME $HOME
USER $UNAME
EXPOSE 5000
# CMD python multiplan/app.py
CMD gunicorn --bind 0.0.0.0:5000 --timeout 600 multiplan.app:server