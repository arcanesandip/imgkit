#!/bin/bash

echo "Setting up imgkit..."

# Create virtual environment
python3 -m venv venv

# Install dependencies inside venv
./venv/bin/pip install --quiet -r requirements.txt

echo ""
echo "Setup complete. Now run:"
echo ""
echo "  source venv/bin/activate"
echo ""
echo "Your prompt will change to (venv). Then run:"
echo ""
echo "  python process.py"
echo ""