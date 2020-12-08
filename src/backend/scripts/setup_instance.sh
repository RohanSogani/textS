#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo apt-get -y install python3-pip

pip3 install --upgrade pip

pip3 install -r /home/ecs289gnlp/textS/src/pegasus/requirements.txt

pip3 install -r /home/ecs289gnlp/textS/requirements.txt