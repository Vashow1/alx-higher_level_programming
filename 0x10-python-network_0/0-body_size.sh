#!/bin/bash
# displays the size of the curl response
curl -s "$1" | wc --bytes
