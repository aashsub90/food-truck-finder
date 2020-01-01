#!/bin/bash

# Create a virtual environment
pip install pip --install --user
pip install virtualenv
virtualenv -p /usr/local/bin/python3 food-truck-env

source ./food-truck-env/bin/activate

# Install requirements
pip install -r requirements.txt

# Create supporting directories
mkdir -p logs
mkdir -p bin

# Create script for env
touch env.sh
echo "export PATH=`pwd`/bin/:$PATH" >> env.sh
echo "export CONFIG_PATH=`pwd`/config/" >> env.sh
echo "export LOG_PATH=`pwd`/logs/" >> env.sh

# Create link to program
ln -s `pwd`/food-truck-finder.py bin/food-truck-finder
