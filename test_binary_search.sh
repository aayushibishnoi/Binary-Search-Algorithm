#!/bin/bash

# Test script for Binary Search Algorithm

# Check if Python is installed
echo "Checking for Python3..."
if ! command -v python3 >/dev/null 2>&1; then
    echo "FAIL: Python3 not found. Install it with 'sudo apt install python3'."
    exit 1
fi
echo "PASS: Python3 found"

# Run the Python script and capture output
echo "Running binary_search.py..."
python3 binary_search.py > output.txt

# Test 1: Check if element 10 is found
echo "Testing search for element 10..."
if grep -q "Element 10 found at index 3" output.txt; then
    echo "PASS: Element 10 found correctly (iterative and recursive)"
else
    echo "FAIL: Element 10 not found"
fi

# Test 2: Check if element 3 is found
echo "Testing search for element 3..."
if grep -q "Element 3 found at index 1" output.txt; then
    echo "PASS: Element 3 found correctly (iterative and recursive)"
else
    echo "FAIL: Element 3 not found"
fi

# Test 3: Check if element 99 is not found
echo "Testing search for element 99..."
if grep -q "Element 99 not found in array" output.txt; then
    echo "PASS: Element 99 correctly reported as not found"
else
    echo "FAIL: Element 99 search failed"
fi

# Test 4: Check for unsorted array handling
echo "Testing unsorted array handling..."
echo "
arr = [4, 2, 10, 3]
target = 10
print(binary_search_iterative(arr, target))
" > temp_test.py

if python3 temp_test.py 2>&1 | grep -q "ValueError: Array must be sorted"; then
    echo "PASS: Unsorted array correctly rejected"
else
    echo "FAIL: Unsorted array not handled"
fi

# Clean up
rm -f output.txt temp_test.py

echo "All tests completed!"
