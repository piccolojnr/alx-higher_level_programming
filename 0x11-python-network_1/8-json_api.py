#!/usr/bin/python3
"""script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    resp = requests.post(url, data={"q": q})
    try:
        resp_dict = resp.json()
        id, name = resp_dict.get("id"), resp_dict.get("name")
        if len(resp_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(resp_dict.get("id"), resp_dict.get("name")))
    except:
        print("Not a valid JSON")
