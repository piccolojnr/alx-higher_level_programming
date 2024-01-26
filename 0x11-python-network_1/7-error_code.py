#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    import requests
    import sys

    with requests.get(sys.argv[1]) as f:
        status = f.status_code
        if status < 400:
            print(f.text)
        else:
            print("Error code: {}".format(f.status_code))
