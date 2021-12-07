#!/bin/bash
docker run --name "temperature_jetsonNano:0.1" \
-d --privileged --net host --restart "always" \
python3 -u temperature_test.py 15 #dt seconds