#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit """
from requests import get


def top_ten(subreddit):
    """ Get first 10 hot posts for a subreddit """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False, headers={'User-Agent': "myKey"},
                   params={'limit': 10})
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
