#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
if [ ! -f "./bin/activate" ]; then
    # no venv found asume instalation required
    echo "installing dependencies..."    
    python3 -m venv .
    source ./bin/activate   
    pip3 install -r requirements.txt
else 
    echo "activating virtual env"    
    source ./bin/activate
fi
python3 ./lana-client.py $@