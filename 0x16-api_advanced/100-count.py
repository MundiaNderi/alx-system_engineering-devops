#!/usr/bin/python3
"""Module for searching keywords in hot titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after_val=None, count_dict=None):
    '''Recursively queries the Reddit API, parses the titles of hot
    articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences
        in the titles.
        after_val (str, optional): The value used for pagination.
        Default is None.
        count_dict (dict, optional): A dictionary to store the count of
        each keyword. Default is None.

    Returns:
        None

    Prints:
        The sorted count of each keyword in descending order.
    '''
    if count_dict is None:
        count_dict = {}

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'
    USERAGENT = {
        'User-Agent': 'Unix:com.alx.apiadvanced:task3 (by /u/_mundia_nderi_)'}
    params = {'limit': 100}

    if after_val:
        params['after'] = after_val

    req = requests.get(URL, headers=USERAGENT, params=params)

    if req.status_code != 200:
        return

    jreq = req.json()
    data_path = jreq['data']['children']

    for post in data_path:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                count_dict[word] = count_dict.get(word, 0) + title.count(word)

    after_val = jreq['data']['after']
    if after_val is None:
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_count:
            print(f"{keyword}: {count}")
    else:
        count_words(subreddit, word_list, after_val, count_dict)
