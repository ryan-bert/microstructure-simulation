#!/bin/bash

# Move to the project root
cd "$(dirname "$0")/.."

# Run all unit tests, setting PYTHONPATH to current directory
PYTHONPATH=. python3 -m unittest discover -s tests