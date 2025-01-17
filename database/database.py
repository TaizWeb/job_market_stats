"""Module containing a class to interact with the database"""

import datetime
import itertools
import sqlite3
import time


class Database:
    """Class for interacting with the database

    Attributes
    ----------
    conn:
        The connection to the database
    cursor:
        The cursor for the database
    comment_ids: list[tuple]
        A list of unique comment IDs, to avoid duplicate API calls

    Methods
    -------
    init_db()
        Initializes the database if it's not already
    get_comment_ids()
        Gets the comment IDs previously obtained in the DB
    add_postings(postings: list)
        Adds `postings` to the database
    query_postings(
        year: int = None,
        month: int = None,
        query: str = None,
        case_sensitive: bool = False,
    )
        Returns a list of results that match the parameters
    dump_database()
        Dumps the entirety of the database's contents, used for debuggging
    """

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
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
        year: int = None
            The year of results to query
        month: int = None
            The month of results to query, e.g. January = 1
        query: str = None
            The term to search by
        case-sensitive: bool = False
            If the term should be case-sensitive, useful for "go" vs "Go"

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

    def dump_database_interval(
        self, start_date: str = "2018-01-01", end_date: str = "2024-01-01"
    ):
        """Dump the entirety of the database's contents per a given time tange

        Parameters
        ----------
        start_date: str = "2018-01-01"
            The starting date of results to fetch
        end_date: str = "2018-01-01"
            The ending date of results to fetch

        Returns
        -------
        results:
            The contents of every row within the DB

        Note
        ----
        The format is in yyyy-MM-dd format
        """
        # Convert to Unix time
        start_time = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
        end_time = int(time.mktime(time.strptime(end_date, "%Y-%m-%d")))

        statement = f"""SELECT * FROM postings WHERE
        year BETWEEN {start_time} AND {end_time};"""
        self.cursor.execute(statement)
        return self.cursor.fetchall()
