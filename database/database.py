"""Database manager"""

import sqlite3


class Database:
    """docstring for Database."""

    def __init__(self):
        self.conn = sqlite3.connect("postings.db")
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        """Initializes the DB if it's not already"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS postings (
                id INTEGER PRIMARY KEY,
                year INTEGER NOT NULL,
                text TEXT NOT NULL UNIQUE
            )
        """
        )

    def add_postings(self, postings: list):
        """Add a posting to the database


        Parameters
        ----------
        postings: list[tuple]
            The postings from the Hackernews API, which should be a list of
            tuples containing (year, text)

        Returns
        -------
        status: bool
            Whether the operation succeeded
        """
        try:
            self.cursor.executemany(
                "INSERT INTO postings (year, text) VALUES (?, ?)", postings
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Encountered DB error {e}")
            return False

    def query_postings(self, year: int = None, query: str = None):
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
        statement = """SELECT * FROM postings WHERE year = ? AND text LIKE ?"""
        params = (year, f"%{query}%")
        self.cursor.execute(statement, params)
        return self.cursor.fetchall()
