#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import pprint
import requests
import sys


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'request'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
