#!/bin/bash

if [[ -d ".env" ]]
then
        echo "Activating virtual environment..."
        source .env/bin/activate
        echo "Virtual environment activated"
else
        echo "Creating virtual environment..."
        virtualenv .env
        echo "Virtual environment created"
	echo "Activating virtual environment..."
	source .env/bin/activate
	echo "Virtual environment activated"
        echo "Loading dependencies..."
        FILE=requirements.txt
        if test -f "$FILE";then
                pip install -r FILE
        else
                echo "There is no $FILE file, failed to load dependencies..."
        fi
fi
echo "Running firstFile.py..."
python firstFile.py
