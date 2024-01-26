#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = " https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    resp = requests.get(url)
    commits = resp.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))
