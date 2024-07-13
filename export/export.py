"""Export class"""

import matplotlib.pyplot as plt
import pandas as pd

# from export import TECHS
from .search_terms import TECHS


class Export:
    """docstring for Export."""

    def __init__(self):
        pass

    def to_csv(
        self,
        database: "Database",
        year_start: int,
        year_end: int,
        month_step: int = 12,
        category: str = None,
        filename: str = "data.csv",
    ):
        """Converts the data at the columns to a CSV

        Parameters
        ----------
        database: Database
            The reference to the database object
        year_start: int
            The starting point of the years to export
        year_end: int
            The ending point of the years to export
        month_step: int
            How often between individual years to export
        category: str
            Which section of search_terms.py to export
        filename: str
            The filename to use for the exported .csv file
        """
        if category is not None:
            data = {"Technology": [], "Count": [], "Year": []}
            for tech in TECHS[category]:
                for year in list(range(year_start, year_end + 1)):
                    data["Technology"].append(tech["name"])
                    data["Year"].append(year)
                    names = [tech["name"]] + tech["aliases"]
                    total_count = 0
                    for name in names:
                        for step in range(int(12 / month_step)):
                            total_count += len(
                                database.query_postings(
                                    year, step, name, tech["case_sensitive"]
                                )
                            )
                    data["Count"].append(total_count)
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)

    def to_plot(self, csv_path):
        """Plots the data to a popup window

        Parameters
        ----------
        csv_path: str
            The path to the .csv file (created from to_csv) to plot
        """
        # Read the CSV data into a DataFrame
        data = pd.read_csv(csv_path)

        # Pivot the data to make it easier to plot
        pivot_data = data.pivot(index="Year", columns="Technology", values="Count")

        # Plotting
        plt.figure(figsize=(10, 6))

        # Line styles, since this many data points is bad
        styles = ["-", "--", "-.", ":"]

        # Plot each technology's data
        for idx, tech in enumerate(pivot_data.columns):
            plt.plot(
                pivot_data.index,
                pivot_data[tech],
                linestyle=styles[idx % len(styles)],
                label=tech,
            )

        # Adding titles and labels
        plt.title("HN Job Requirements Over Time")
        plt.xlabel("Year")
        plt.ylabel("Job Postings")
        plt.legend(title="Technology")

        # Show the plot
        plt.show()
