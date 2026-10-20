# LocalStack notes

## Start LocalStack
docker run --rm -d -p 4566:4566 -v /var/run/docker.sock:/var/run/docker.sock --name localstack localstack/localstack

## Fake credentials
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_DEFAULT_REGION=us-east-1

## Check it is running
curl http://localhost:4566/_localstack/health

## Stop it
docker stop localstack