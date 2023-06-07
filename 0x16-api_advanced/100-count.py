#!/usr/bin/python3
"""Module for searching keywords in hot titles of a subreddit."""

import requests


def count_words(subreddit, word_list, count=0, after_val=None):
    '''Searches for keywords in hot titles of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to search for in the
        titles of hot articles.
        count (int, optional): The number of recursive calls made.
        Default is 0.
        after_val (str, optional): The value used for pagination.
        Default is None.

    Returns:
        int: The total count of occurrences of the keywords
        in the titles of hot articles.
    '''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {
        'User-Agent': 'Unix:com.alx.apiadvanced:task3 (by /u/_mundia_nderi_)'}
    params = {'limit': 100}

    # Rest of the code...
