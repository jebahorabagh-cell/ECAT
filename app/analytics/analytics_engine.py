"""
------------------------------------------------------------
ECAT - Excel Comparison & Audit Tool
Analytics Engine
Build : 1.0.6
------------------------------------------------------------
"""

import pandas as pd


class AnalyticsEngine:
    """
    Core analytics engine.

    All reports in ECAT will use this engine.
    """

    # --------------------------------------------------

    def filter_data(self, df, filters=None):
        """
        Apply filters.

        Example:
        filters = {
            "Tariff": "LV1",
            "Status": "Active"
        }
        """

        if filters is None:
            return df

        result = df

        for column, value in filters.items():

            if column not in result.columns:
                continue

            result = result[result[column] == value]

        return result

    # --------------------------------------------------

    def group_by(
        self,
        df,
        rows,
        values,
        aggregation="sum",
        filters=None
    ):
        """
        Generic Group By engine.
        """

        df = self.filter_data(df, filters)

        agg_map = {
            "sum": "sum",
            "count": "count",
            "mean": "mean",
            "min": "min",
            "max": "max",
            "median": "median",
            "std": "std",
            "var": "var",
            "nunique": "nunique"
        }

        if aggregation not in agg_map:
            raise ValueError(
                f"Unsupported aggregation : {aggregation}"
            )

        result = (
            df.groupby(rows)[values]
            .agg(agg_map[aggregation])
            .reset_index()
        )

        return result

    # --------------------------------------------------

    def compare_values(
        self,
        current,
        previous
    ):
        """
        Returns Difference and % Change.
        """

        diff = current - previous

        if previous == 0:
            pct = None
        else:
            pct = (diff / previous) * 100

        return diff, pct