#!/bin/bash

if [[ -d ".env" ]]
then
	echo "Activating virtual environment..."
	source .env/bin/activate
	ls
	echo "Virtual environment activated"
else
	echo "Creating virtual environment ..."
	virtualenv .env
	pip freeze > requirements.txt
	echo "Virtual environment created"
	echo "Run main.py"
	python main.py
fi
