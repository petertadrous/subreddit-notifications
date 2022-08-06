# Subreddit Notifications Script

## About

This project is intended to monitor new submissions of a given subreddit, and post content to a discord webhook when specified keywords appear in the title of a new submission.

## Requirements

The required packages are:

* pip
* pyyaml
* praw
* discordwebhook

## Usage

1. Rename `secrets_template.yaml` to `secrets.yaml` and fill in with both the reddit API parameters, and the discord webhook URL.
2. Modify the parameters in `driver.py` in the final section of code to adjust for your desired search:
   1. `secret_file`: string, by default ".\secrets.yaml"
   2. `subreddit_name`: string, name of subreddit to monitor
      * To monitor more than one subreddit, concatenate both sub names with "+" as one string
   3. `keywords_list`: list of strings (lowercase), keywords to find in title
   4. `keyword_search_type`: string, either "all" or "any"
3. Run script with  
    `> python driver.py`

## License

MIT License  
Copyright (c) 2022 petertadrous

## Contact

Peter Tadrous - petertadrous@gmail.com  
Project Link: <https://github.com/petertadrous/subreddit-notifications>
