#!/usr/bin/python3
"""recursive function queries the Reddit API, parses the title of all hot
   articles, and prints a sorted count of given keywords (case-insensitive,
   delimited by spaces """
from requests import get


def count_words(subreddit, word_list, params={}, hot_list=[], counter=0):
    """ Get titles of all hot articles for a given subreddit """
    print(counter)

    if (params.get('after') is None and counter != 0):
        for word in word_list:
            found = 0
            for title in hot_list:
                found += title.upper().count(word.upper())
            if found != 0:
                print("{}: {}".format(word, found))
        return

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    response = get(url, allow_redirects=False, headers={'User-Agent': "myKey"},
                   params=params)
    if response.status_code == 404:
        return

    params['after'] = response.json().get('data').get('after')
    params['before'] = response.json().get('data').get('before')

    for res in response.json().get("data").get('children'):
        hot_list.append(res.get("data").get("title"))
    counter += 1
    return count_words(subreddit, word_list, params, hot_list, counter)
