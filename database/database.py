"""Database manager"""

import datetime
import itertools
import sqlite3


class Database:
    """docstring for Database."""

    def __init__(self):
        self.conn = sqlite3.connect("postings.db")
        self.cursor = self.conn.cursor()
        self.init_db()
        self.comment_ids = list(itertools.chain(*self.get_comment_ids()))

    def init_db(self):
        """Initializes the DB if it's not already"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS postings (
                id INTEGER PRIMARY KEY,
                comment_id INTEGER NOT NULL UNIQUE,
                year INTEGER NOT NULL,
                text TEXT NOT NULL UNIQUE
            )
        """
        )

    def get_comment_ids(self):
        """Gets all unique thread ids, to save time"""
        statement = """SELECT comment_id FROM postings;"""
        self.cursor.execute(statement)
        return self.cursor.fetchall()

    def add_postings(self, postings: list):
        """Add a posting to the database


        Parameters
        ----------
        postings: list[dict]
            The postings from the Hackernews API, which should be a list of
            dicts containing keys for post_id, post_year, and post_text

        Returns
        -------
        status: bool
            Whether the operation succeeded
        """
        for posting in postings:
            try:
                self.cursor.execute(
                    (
                        "INSERT INTO postings (comment_id, year, text) VALUES "
                        "(:post_id, :post_time, :post_text)"
                    ),
                    posting,
                )
                self.conn.commit()
            except (sqlite3.IntegrityError, ValueError) as e:
                print(f"Encountered DB error {e}")
                print(f"Cause was {posting}")
        return True

    def query_postings(
        self,
        year: int = None,
        month: int = None,
        query: str = None,
        case_sensitive: bool = False,
    ):
        """Get the postings fitting the parameters

        Parameters
        ----------
        year: int
            The year of results to query
        query: str
            The term to search by

        Returns
        -------
        results:
            The matching results from the query
        """
        if case_sensitive:
            params = (str(year), f"{month:02}", f"*{query}*")
            text_form = "GLOB"
        else:
            params = (str(year), f"{month:02}", f"%{query}%")
            text_form = "LIKE"
        statement = f"""SELECT * FROM postings
        WHERE strftime('%Y', datetime(year, 'unixepoch')) = ?
        AND strftime('%m', datetime(year, 'unixepoch')) = ?
        AND text {text_form} ?"""
        self.cursor.execute(statement, params)
        return self.cursor.fetchall()

    def dump_database(self):
        """Dump the entirety of the database's contents

        Returns
        -------
        results:
            The contents of every row within the DB
        """
        statement = """SELECT * FROM postings;"""
        self.cursor.execute(statement)
        return self.cursor.fetchall()
