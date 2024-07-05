"""Main module"""

from database import Database
from hn_api import Api

db = Database()
api = Api()

threads = api.get_hiring_threads(10)
comments = api.get_top_level_comments(threads[0])
print(api.get_user_thread_link(comments[0]))
print(api.get_thread_desc(comments[0]))
print("Trying DB")
db.init_db()
db.query_postings()
# print(get_hiring_threads(10))
