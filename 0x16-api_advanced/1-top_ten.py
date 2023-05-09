#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit """
from requests import get


def top_ten(subreddit):
    """ Get first 10 hot posts for a subreddit """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False, headers={'User-Agent': "myKey"}, params={'limit': 10})
    if response.status_code == 404:
        print(None)
        return

    for res in response.json().get("data").get('children'):
        print(res.get("data").get("title"))
