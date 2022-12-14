#!/bin/bash

sudo apt install python3 python3-pip python3-venv chromium-browser wget unzip -y

version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html

while getopts "c" opt; do
    case ${opt} in 
        c) echo -e "python3 create.py\n" >> deployment-script.sh;;
    esac
done

echo "python3 -m gunicorn -D --bind 0.0.0.0:5000 --workers 4 app:app" >> deployment-script.sh

ssh jenkins@prod-server < deployment-script.sh