# upload_data.py
"""Uploads data from source to postgres"""

# import standard libraries

import subprocess
import sys
import os
from time import time
import argparse

# import non-standard libraries

def install_requirements(packages):
    """
    Installs required packages using pip

    Args:
        packages (array): list of packages to be installed
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

try:
    import pandas as pd
    from sqlalchemy import create_engine
except ImportError:
    install_requirements(["sqlalchemy", "psycopg2", "pandas"])

# ingest data from source to postgres

def main(params):
    """
    Ingests data from source to postgres

    Args:
        user (string): postgres user
        password (string): postgres password
        hostname (string): postgres hostname
        port(integer): postgres port
        database(string): postgres target database
        table(string): postgres target table
        url(string): url of source data
        filename(string): filename of source data
    """
    user = params.user
    password = params.password
    hostname = params.hostname
    port = params.port
    database = params.database
    table = params.table
    url = params.url
    filename = params.filename

    os.system(f"wget {url} -O {filename}")

    engine = create_engine(f"postgresql://{user}:{password}@{hostname}:{port}/{database}")

    df_iterator = pd.read_csv(filename, compression='gzip', iterator=True, chunksize=100000)

    df = next(df_iterator)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table, con=engine, if_exists='replace')

    count = 1

    # partition file upload into smaller chunks due to size

    while True:

        try:
            started_at = time()

            df = next(df_iterator)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table, con=engine, if_exists='append')

            finished_at = time()

            duration = finished_at - started_at

            print(f'Partition {count} successfully loaded in {duration:.3f} seconds')

            count += 1

        except StopIteration:
            row_count = pd.read_sql(f"SELECT COUNT(*) FROM {table}", con=engine)
            print(f"{row_count} rows sucessfully loaded")
            break

# run script and set parameters

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='postgres user')
    parser.add_argument('--password', required=True, help='postgres password')
    parser.add_argument('--hostname', required=True, help='postgres hostname')
    parser.add_argument('--port', required=True, help='postgres port')
    parser.add_argument('--database', required=True, help='postgres target database')
    parser.add_argument('--table', required=True, help='postgres target table')
    parser.add_argument('--url', required=True, help='url of source data')
    parser.add_argument('--filename', required=True, help='filename of source data')

    args = parser.parse_args()

    main(args)
