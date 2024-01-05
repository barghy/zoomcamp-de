# run.sh
echo "Setting parameters..."
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

echo "Ingesting data..."
docker run -it \
  --network=pg-network \
  load_data:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --database=ny_taxi \
    --table=green_taxi_trips \
    --url=${URL} \
    --filename=green_tripdata_2019-01.csv.gz