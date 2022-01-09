#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of
a repository by a user
"""

import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
           owner_name,
           repo_name)
    params = {'per_page': 10}
    headers = {'Accept': 'application/vnd.github.v3+json'}

    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    for commit in data:
        print(commit['sha'] + ':', commit['commit']['author']['name'])
