#!/usr/bin/env bash

IMAGE_NAME=reljicd/docker-blog
echo -e "\nSet docker image name as ${IMAGE_NAME}\n"
PORT=8000
echo -e "Set docker image PORT to ${PORT}\n"

echo -e "\nStop running Docker containers with image name ${IMAGE_NAME}...\n"
docker stop $(docker ps -a | grep ${IMAGE_NAME} | awk '{print $1}')

echo -e "\nDocker build image with name ${IMAGE_NAME}...\n"
docker build -t ${IMAGE_NAME} -f docker/Dockerfile .

echo -e "\nStart Docker container of the image ${IMAGE_NAME}...\n"
docker run --rm -i -p ${PORT}:${PORT} ${IMAGE_NAME}