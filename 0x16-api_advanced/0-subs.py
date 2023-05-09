#!/usr/bin/python3
"""Queries the Reddit API and returns number of subscribers for a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """ Get subscribers of a subreddit """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = get(url, headers={'User-agent': "myKey"}, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    res = response.json().get("data").get("subscribers")

    return (res)
