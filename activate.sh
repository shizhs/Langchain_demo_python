#!/bin/bash
# Convenience script to activate the Python virtual environment
# Usage: source activate.sh

echo "Activating Python virtual environment..."
source venv/bin/activate
echo "Virtual environment activated!"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"
echo ""
echo "To deactivate the environment, run: deactivate"
echo "To install additional packages, run: pip install <package_name>"