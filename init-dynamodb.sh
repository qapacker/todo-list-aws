#!/bin/sh
echo "Esperando a que DynamoDB esté disponible..."
until curl -s http://dynamodb:8000 > /dev/null; do
  echo "Still waiting..."
  sleep 1
done

echo "DynamoDB disponible. Creando tabla..."

export AWS_ACCESS_KEY_ID=dummy
export AWS_SECRET_ACCESS_KEY=dummy
export AWS_DEFAULT_REGION=us-east-1

aws dynamodb create-table \
  --table-name local-TodosDynamoDbTable \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
  --endpoint-url http://dynamodb:8000 \
  || echo 'La tabla ya existe o hubo un error controlado.'
