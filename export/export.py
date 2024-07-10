"""Export class"""

import pandas as pd

# from export import TECHS
from .search_terms import TECHS


class Export:
    """docstring for Export."""

    def __init__(self):
        pass

    def to_csv(
        self,
        database,
        year_start: int,
        year_end: int,
        category: str = None,
        filename: str = "data.csv",
    ):
        """Converts the data at the columns to a CSV"""
        if category is not None:
            data = {"Technology": [], "Count": [], "Year": []}
            for tech in TECHS[category]:
                for year in list(range(year_start, year_end + 1)):
                    data["Technology"].append(tech["name"])
                    data["Year"].append(year)
                    names = [tech["name"]] + tech["aliases"]
                    total_count = 0
                    for name in names:
                        total_count += len(
                            database.query_postings(year, name, tech["case_sensitive"])
                        )
                    data["Count"].append(total_count)
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
