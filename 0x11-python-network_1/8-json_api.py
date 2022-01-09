#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = "" if len(sys.argv) == 1 else sys.argv[1]

    res = requests.post(url, data={'q': query})
    try:
        data = res.json()
        if data == {} or data.get('id') is None:
            print('No result')
        else:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
    except Exception:
        print("Not a valid JSON")
