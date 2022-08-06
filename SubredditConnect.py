import praw
import yaml
from typing import Dict, Iterator


def load_creds(
        file: str
) -> praw.reddit:
    with open(file) as file:
        auth = yaml.load(file, Loader=yaml.FullLoader)

    return praw.Reddit(
        client_id=auth['client_id'],
        client_secret=auth['client_secret'],
        user_agent=auth['user_agent'],
        password = auth['password'],
        username = auth['username']
    )


def subreddit_connect(
        reddit: praw.reddit,
        subreddit: str
) -> praw.reddit.Subreddit:

    return reddit.subreddit(subreddit)


def new_posts(
        subreddit: praw.reddit.Subreddit,
        kwargs = Dict
) -> Iterator:
    return subreddit.new(**kwargs)


def new_stream(
        subreddit: praw.reddit.Subreddit
) -> Iterator:
    return subreddit.stream.submissions()


def load_new_posts(
        secrets_file: str,
        subreddit_name: str,
        new_post_kwargs: Dict = {}
) -> Iterator:
    reddit = load_creds(secrets_file=secrets_file)
    subreddit = subreddit_connect(
        reddit=reddit,
        subreddit=subreddit_name
    )
    return new_posts(
        subreddit=subreddit,
        kwargs=new_post_kwargs
    )


def stream_new_posts(
    secrets_file: str,
    subreddit_name: str
) -> Iterator:
    reddit = load_creds(file=secrets_file)
    subreddit = subreddit_connect(
        reddit=reddit,
        subreddit=subreddit_name
    )
    return new_stream(subreddit=subreddit)