#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your i
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    personal_token = sys.argv[2]
    headers = {'Authorization': 'token {}'.format(personal_token)}
    res = requests.get('https://api.github.com/user', headers=headers)
    print(res.json().get('id'))
