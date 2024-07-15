"""Module to handle interaction with the HackerNews API"""

import json
import urllib.request


class Api:
    """Class for interacting with the HN API

    Attributes
    ----------
    api_link: str
        The link to the API endpoint
    bot_id: str
        The name of the hiring bot to scrape posts from

    Methods
    -------
    link_to_json(link)
        Converts a link into a JSON dictionary containing the API info
    get_user_thread_link(thread_id: str)
        Gets a user-friendly link from a thread_id
    is_hiring_thread(thread_id: str)
        Dictates if the thread is actually a hiring thread
    get_hiring_threads(thread_count: int = None, offset: int = None)
        Gets a list of hiring thread IDs and returns it
    get_top_level_comments(thread_id: str, child_count: int = None)
        Gets a list of top-level comment IDs of thread_id
    get_thread_info(thread_id: str)
        Gets info of a thread, namely the id, time, and text. Used for the DB
    """

    def __init__(self, api_link: str, bot_id: str):
        self.api_link = api_link
        self.bot_id = bot_id

    def link_to_json(self, link: str):
        """Get a link, convert it to a JSON dict, and return it

        Parameters
        ----------
        link: str
            The link to convert to a JSON dict

        Returns
        -------
        response: dict
            The HTTP response in JSON format
        """
        request = urllib.request.Request(link)
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read())

    def get_user_thread_link(self, thread_id: str):
        """Give a thread ID, get a link to the real HN site

        Parameters
        ----------
        thread_id: str
            The ID of the HN thread

        Returns
        -------
        api_link: str
            The user-friendly link to the context
        """
        return f"https://news.ycombinator.com/item?id={thread_id}"

    def is_hiring_thread(self, thread_id: str):
        """Is this actually a hiring thread??"""
        thread_link = f"{self.api_link}/item/{thread_id}.json"
        try:
            return "Ask HN: Who is hiring?" in self.link_to_json(thread_link)["title"]
        except KeyError:
            print(f"Error: {thread_link} is not a valid post")
            return False

    def get_hiring_threads(self, thread_count: int = None, offset: int = None):
        """Returns a list of hiring thread ids

        Parameters
        ----------
        thread_count: int
            How many threads IDs to return

        Returns
        -------
        thread_list: list[str]
            A list of hiring thread IDs
        """
        json_link = f"{self.api_link}/user/{self.bot_id}.json"
        thread_ids = self.link_to_json(json_link)["submitted"]
        return [
            thread_id for thread_id in thread_ids if self.is_hiring_thread(thread_id)
        ][offset : offset + thread_count]

    def get_top_level_comments(self, thread_id: str, child_count: int = None):
        """Returns a list of direct children IDs on a post

        Parameters
        ----------
        thread_id: str
            The ID of the thread
        child_count: int
            How many top-level child comments to return

        Returns
        -------
        child_links: list[str]
            A list of child comment IDs
        """
        parent_link = f"{self.api_link}/item/{thread_id}.json"
        return self.link_to_json(parent_link)["kids"][:child_count]

    def get_thread_info(self, thread_id: str):
        """Gets a thread's information (id, time, text)

        Parameters
        ----------
        thread_id: str
            The ID of the thread

        Returns
        -------
        post_contents: dict | bool
            A dict containing the post's id, creation time, and body text. If
            this doesn't work, return `False`
        """
        parent_link = f"{self.api_link}/item/{thread_id}.json"
        parent_json = self.link_to_json(parent_link)
        # Dead/deleted posts are still returned, handling them
        if "deleted" in parent_json:
            return False

        try:
            post_dict = {
                "post_id": int(thread_id),
                "post_time": int(parent_json["time"]),
                "post_text": parent_json["text"],
            }
            return post_dict
        except KeyError:
            print("KEY ERR")
            print(parent_json)
            return False
