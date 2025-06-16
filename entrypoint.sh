#!/bin/bash
set -e
sam build
sam local start-api \
  --host 0.0.0.0 \
  --port 3000 \
  --env-vars localEnvironment.json
