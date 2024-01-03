# Zoomcamp: Data Engineering

`Total Duration: 2hr 31m`
[Introduction](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup)

## Docker

`Duration: 24m`
[Introduction to Docker](https://www.youtube.com/watch?v=EYNwNlOrpr0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

- Generate Dockerfile - without a file extension
- `docker build -t test:pandas .` - must be in the same directory as the Dockerfile
- `docker run -it test:pandas`
- `python`
- `import pandas`
- `pandas.__version__`
- Create pipeline.py
- Update Dockerfile as per below

```dockerfile
WORKDIR /app 
COPY pipeline.py pipeline.py
```

- `docker build -t test:pandas .`
- `docker run -it test:pandas`
- `python pipeline.py`
- Update pipeline.py to accept terminal parameters

```python
import sys
print(sys.argv)
day = sys.argv[1]
print(f'Success : Job Completed Sucessfully for {day}')
```

- Update Dockerfile `ENTRYPOINT [ "python", "pipeline.py" ]`
- `docker build -t test:pandas .`
- `docker run -it test:pandas 2024-01-03`

## Postgres

`Duration: 29m`

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/postgres_data_ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

## pgAdmin & Postgres

`Duration: 11m`

## Ingestion Script

`Duration: 19m`

## Docker Compose

`Duration: 9m`

## SQL

`Duration: 16m`

## Docker Port Mapping and Networks

`Duration: 16m`

## WSL: Windows Subsystem for Linux

`Duration: 7m`
