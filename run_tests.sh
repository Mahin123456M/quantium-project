#!/bin/bash


echo "Starting Dash App Test Suite..."

# Activate virtual environment
powershell.exe -Command "Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned; & 'venv/Scripts/Activate.ps1'"

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

echo "Virtual environment activated successfully"


cd src

if [ $? -ne 0 ]; then
    echo "Failed to change to src directory"
    exit 1
fi

echo "Changed to src directory"


echo "Running test suite..."
python -m pytest test_app.py -v

# Capture the exit code
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Some tests failed or encountered errors"
    exit 1
fi