#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit """
from requests import get


def recurse(subreddit, hot_list=[], params={}, counter=0):
    """ Get titles of all hot articles for a given subreddit """
    if (params.get('after') is None and counter != 0):
        return hot_list

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False, headers={'User-Agent': "myKey"},
                   params=params)
    if response.status_code == 404:
        return None
    params['after'] = response.json().get('data').get('after')
    params['before'] = response.json().get('data').get('before')

    for res in response.json().get("data").get('children'):
        hot_list.append(res.get("data").get("title"))
    counter += 1
    return recurse(subreddit, hot_list, params, counter)
