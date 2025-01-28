FROM apache/airflow:2.7.3-python3.10

USER root

# Installing required dependencies for the project
# Had issues with psycopg2 without these libs
RUN set -ex && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libpq-dev \
        postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

# Python packages needed for the project
# Removed version constraints after dependency conflicts
RUN pip install --no-cache-dir \
    apache-airflow-providers-postgres \
    psycopg2-binary \
    meltano