import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if not isinstance(subreddit, str):
        return 0
    
    url_api = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'safari:holberton/0.1.0'}
    
    response = requests.get(url_api, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json()["data"]
        subscribers = data["subscribers"]
        return subscribers
    except (KeyError, ValueError):
        return 0


