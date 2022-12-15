#!/bin/bash
# sends a DELETE request to the url passed as the first arg
curl -s -XDELETE "$1"
