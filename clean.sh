#!/bin/bash

echo "Cleaning up imgkit..."

# Clear input folder
rm -f input/*

# Remove output/images folder and all processed images
rm -rf output/images

echo "Done. input/ and output/images/ have been cleared."