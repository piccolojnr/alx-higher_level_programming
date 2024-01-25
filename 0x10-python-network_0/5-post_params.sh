#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
