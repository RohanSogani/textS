#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo apt-get -y install python3-pip

pip3 install --upgrade pip

cd ../pegasus/

pip3 install -r requirements.txt

cd ../../

pip3 install -r requirements.txt