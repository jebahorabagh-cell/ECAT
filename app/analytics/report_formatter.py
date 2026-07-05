"""
------------------------------------------------------------
ECAT
Report Formatter
Build : 1.1.2
------------------------------------------------------------
"""

import pandas as pd

from app.config.business_rules import (
    FEEDERS,
    FEEDER_ORDER,
    ZONE_1,
    ZONE_2,
    ZONE_NAMES
)


class ReportFormatter:

    def __init__(self):
        pass

    # -----------------------------------------------------

    def format(self, df):

        """
        Receives a dataframe grouped by Location Code.

        Example Input

        Location Code | Apr | May
        --------------------------------
        1444201         100     120
        1444202         200     180

        Returns

        Feeder | Apr | May
        ----------------------------
        HROSE DC(T)
        RIDGE DC(T)
        ...

        ZONE 1 SUMMARY

        ...

        DIVISION SUMMARY
        """

        if df.empty:
            return df

        report = []

        numeric_columns = [
            c for c in df.columns
            if c != "Location Code"
        ]

        # -------------------------------------------------
        # Feeder rows
        # -------------------------------------------------

        for loc in FEEDER_ORDER:

            row = df[
                df["Location Code"] == loc
            ]

            if row.empty:
                continue

            record = row.iloc[0].to_dict()

            record["Feeder"] = FEEDERS.get(
                loc,
                str(loc)
            )

            del record["Location Code"]

            report.append(record)

            # ---------------------------------------------
            # Zone 1 Summary
            # ---------------------------------------------

            if loc == ZONE_1[-1]:

                zone = df[
                    df["Location Code"].isin(
                        ZONE_1
                    )
                ]

                total = {
                    "Feeder":
                    ZONE_NAMES["ZONE_1"]
                }

                for col in numeric_columns:
                    total[col] = zone[col].sum()

                report.append(total)

            # ---------------------------------------------
            # Zone 2 Summary
            # ---------------------------------------------

            if loc == ZONE_2[-1]:

                zone = df[
                    df["Location Code"].isin(
                        ZONE_2
                    )
                ]

                total = {
                    "Feeder":
                    ZONE_NAMES["ZONE_2"]
                }

                for col in numeric_columns:
                    total[col] = zone[col].sum()

                report.append(total)

        # -------------------------------------------------
        # Division Summary
        # -------------------------------------------------

        division = {
            "Feeder":
            ZONE_NAMES["DIVISION"]
        }

        for col in numeric_columns:
            division[col] = df[col].sum()

        report.append(division)

        columns = ["Feeder"] + numeric_columns

        return pd.DataFrame(
            report,
            columns=columns
        )