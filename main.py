"""Main module"""

import itertools

from database import Database
from export import Export
from hn_api import Api

BASE_API_LINK = "https://hacker-news.firebaseio.com/v0"
HIRING_BOT_ID = "whoishiring"

db = Database()
api = Api(BASE_API_LINK, HIRING_BOT_ID)
export = Export()


def collect_data(thread_count: int, offset: int = 0):
    """Collect the data and add it to the DB"""
    # The past N months of threads
    threads = api.get_hiring_threads(thread_count, offset)
    threads = [thread for thread in threads if thread not in db.comment_ids]
    # Getting the child comment IDs for each thread
    comments = [api.get_top_level_comments(thread) for thread in threads]
    flattened_comments = list(itertools.chain(*comments))

    # Getting the content of the posts
    print("Getting posts dicts...")
    post_dicts = [api.get_thread_info(comment) for comment in flattened_comments]

    # Adding them to the DB
    db.add_postings(post_dicts)


def get_results(search_year: int, search_term: str):
    """Get the results provided a year and term"""
    # Database queries
    print("Contacting DB")
    print(
        f"'{search_term}' has {len(db.query_postings(search_year, search_term))} results for {search_year}"
    )


# Add more entries to the DB
# collect_data(thread_count=30, offset=40)
# NOTE: Got first 70/158

# get_results(2023, "Javascript")
# get_results(2022, "Javascript")
export.to_csv(db, 2020, 2023, "languages", "refined.csv")
