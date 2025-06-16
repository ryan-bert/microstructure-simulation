#!/bin/bash

# Go to project root directory
cd "$(dirname "$0")/../.."

# Run the speed test directly with correct PYTHONPATH
PYTHONPATH=. python3 tests/speed_tests/speed_test.py