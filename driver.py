import pandas as pd
import numpy as np
import time
from typing import Dict, List


from SubredditConnect import stream_new_posts
from DiscordNotifications import post_content


def track_new_posts(
        secret_file: str,
        subreddit_name: str,
        kwd_list: List,
        kwd_search_type: str,
        get_per_hour: int = 30
) -> None:
    
    found_post_fstr = 'New Deal Found!\nTitle: "{t}"\nLink: "{l}"\nMatched: {k}'

    if kwd_search_type == 'all':
        kwd_srch = all
    elif kwd_search_type == 'any':
        kwd_srch = any
    else:
        raise ValueError('Keyword search type must be either "all" or "any"')

    new_posts = stream_new_posts(
        secrets_file=secret_file,
        subreddit_name=subreddit_name,
    )

    ## parse new posts to see if keywords in title
    for post in new_posts:
        if kwd_srch([k in str.lower(post.title) for k in kwd_list]):
            ## if in title, notify
            post_content(
                file=secret_file,
                content=found_post_fstr.format(
                    t=post.title,
                    l=post.url,
                    k=[k for k in kwd_list if k in str.lower(post.title)]
                )
            )


if __name__ == "__main__":
    secret_file = '.\secrets.yaml'
    subreddit_name = 'buildapcsales'
    keywords_list = ['42','oled','monitor']
    keyword_search_type = 'all'
    get_per_hour = 30
    
    track_new_posts(
        secret_file=secret_file,
        subreddit_name=subreddit_name,
        kwd_list=keywords_list,
        kwd_search_type=keyword_search_type,
        get_per_hour=get_per_hour
    )
