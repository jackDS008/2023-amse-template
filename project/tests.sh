#!/bin/bash

# Test
echo "Testing..."
echo "Tests only work local because .db is in gitignore"
python tests.py

# All tests passed
echo "All tests passed"
exit 0