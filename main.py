"""Main module"""

import json
import urllib.request

from database import Database

BASE_API_LINK = "https://hacker-news.firebaseio.com/v0"
HIRING_BOT_ID = "whoishiring"


def link_to_json(link: str):
    """Get a link, convert it to a JSON dict, and return it"""
    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


def get_user_thread_link(thread_id: str):
    """Give a thread id, get a link to the real HN site"""
    return f"https://news.ycombinator.com/item?id={thread_id}"


def get_hiring_threads(thread_count: int = None):
    """Returns a list of thread id"""
    json_link = f"{BASE_API_LINK}/user/{HIRING_BOT_ID}.json"
    return link_to_json(json_link)["submitted"][:thread_count]


def get_top_level_comments(thread_id: str, child_count: int = None):
    """Returns a list of direct children IDs on a post"""
    parent_link = f"{BASE_API_LINK}/item/{thread_id}.json"
    return link_to_json(parent_link)["kids"][:child_count]


def get_thread_desc(thread_id: str):
    """Gets a thread's description"""
    parent_link = f"{BASE_API_LINK}/item/{thread_id}.json"
    return link_to_json(parent_link)["text"]


def determine_job_skills(comment_body: str):
    pass


db = Database()
threads = get_hiring_threads(10)
comments = get_top_level_comments(threads[0])
print(get_user_thread_link(comments[0]))
print(get_thread_desc(comments[0]))
print("Trying DB")
db.init_db()
db.query_postings()
# print(get_hiring_threads(10))
