#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
