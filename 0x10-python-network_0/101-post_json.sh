#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument
curl -s -XPOST -H "Content-Type: application/json" -d @"$2" "$1"
