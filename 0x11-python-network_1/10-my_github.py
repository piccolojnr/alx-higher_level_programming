#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = "https://api.github.com/users/{}".format(sys.argv[1])
    resp = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(resp.json().get("id"))
