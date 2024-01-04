# init.sh
echo "Creating database containers..."
docker-compose up -d

echo "Creating python containers..."
docker build -t load_data:v001 .
