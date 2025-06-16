#!/bin/bash

# Go to project root directory
cd "$(dirname "$0")/../.."

# Run unit tests in tests/unit_tests with access to src
PYTHONPATH=. python3 -m unittest discover -s tests/unit_tests -p "test_*.py"