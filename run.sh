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
        if test -f "requirements.txt";then
                pip install -r "requirements.txt"
                echo "Dependencies installed"
                echo "Running firstFile.py..."
                python firstFile.py
        else
                echo "There is no requirements.txt file, failed to load dependencies..."
        fi
fi
