# run.sh
echo "Setting parameters..."
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

echo "Ingesting data..."
docker run -it \
  --network=pg-network \
  load_data:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --database=ny_taxi \
    --table=yellow_taxi_trips \
    --url=${URL} \
    --filename=yellow_tripdata_2021-01.csv.gz