"""
------------------------------------------------------------
ECAT
Summary Engine
Build : 1.2.3
------------------------------------------------------------
"""

import pandas as pd

from app.config import business_rules


class SummaryEngine:

    def add_summaries(self, df):

        if df.empty:
            return df

        first_column = df.columns[0]

        numeric_columns = list(df.columns[1:])

        result = []

        # -----------------------------
        # Zone 1
        # -----------------------------

        zone1 = df[
            df[first_column].isin(
                business_rules.ZONE_1
            )
        ]

        result.append(zone1)

        zone1_total = self._summary_row(
            zone1,
            "ZONE 1 SUMMARY",
            numeric_columns,
            first_column
        )

        result.append(zone1_total)

        # -----------------------------
        # Zone 2
        # -----------------------------

        zone2 = df[
            df[first_column].isin(
                business_rules.ZONE_2
            )
        ]

        result.append(zone2)

        zone2_total = self._summary_row(
            zone2,
            "ZONE 2 SUMMARY",
            numeric_columns,
            first_column
        )

        result.append(zone2_total)

        # -----------------------------
        # Division
        # -----------------------------

        division = self._summary_row(
            df,
            "DIVISION SUMMARY",
            numeric_columns,
            first_column
        )

        result.append(division)

        return pd.concat(
            result,
            ignore_index=True
        )

    # --------------------------------------------------

    def _summary_row(
        self,
        df,
        title,
        numeric_columns,
        first_column
    ):

        row = {}

        row[first_column] = title

        for col in numeric_columns:

            row[col] = df[col].sum()

        return pd.DataFrame([row])