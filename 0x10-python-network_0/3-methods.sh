#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.

curl -sI 0.0.0.0 | grep "Allow" | cut -d " " -f2- 
