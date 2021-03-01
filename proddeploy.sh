#!/bin/bash
rm -rf dist/*

# Build new 
python -m build 

# Deploy to PyPi.org
twine upload dist/*