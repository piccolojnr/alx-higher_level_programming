#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    with requests.get("https://alx-intranet.hbtn.io/status") as resp:
        print("Body response:")
        print("\t- type: {}".format(type(resp.content)))
        print("\t- content: {}".format(resp.content))
        print("\t- utf8 content: {}".format(resp.content.decode("utf-8")))
