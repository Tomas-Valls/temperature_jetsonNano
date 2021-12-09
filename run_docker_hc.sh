#!/bin/bash
sudo docker build -t temperature_jetsonnano:0.1 . \
docker run  "temperature_jetsonnano:0.1" \
python3 -u temperature_test.py 15 