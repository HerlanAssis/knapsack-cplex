#!/bin/bash

docker build --tag herlanassis/pythonknapsackcplex .;
docker run -it herlanassis/pythonknapsackcplex bash;