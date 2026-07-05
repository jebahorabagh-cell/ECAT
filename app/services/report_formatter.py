"""
------------------------------------------------------------
ECAT
Report Formatter
Build : 1.2.2
------------------------------------------------------------
"""

import pandas as pd

from app.config import business_rules


class ReportFormatter:

    # --------------------------------------------------

    def format(self, df):

        print("\n========== REPORT FORMATTER ==========")

        print("\nInput")
        print(df.head())

        if df.empty:
            return df

        df = self._replace_feeder_names(df)

        print("\nAfter Mapping")
        print(df.head())

        df = self._sort_feeders(df)

        print("\nAfter Sorting")
        print(df.head())

        print("\n======================================")

        return df

    # --------------------------------------------------

    def _replace_feeder_names(self, df):

        location_column = df.columns[0]

        df[location_column] = (
            df[location_column]
            .apply(business_rules.feeder_name)
        )

        return df

    # --------------------------------------------------

    def _sort_feeders(self, df):

        feeder_order = [
            business_rules.feeder_name(code)
            for code in business_rules.feeder_sequence()
        ]

        location_column = df.columns[0]

        df[location_column] = pd.Categorical(
            df[location_column],
            categories=feeder_order,
            ordered=True
        )

        df = df.sort_values(location_column)

        df[location_column] = df[location_column].astype(str)

        df = df.reset_index(drop=True)

        return df