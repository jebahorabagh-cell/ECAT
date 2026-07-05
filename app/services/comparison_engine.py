"""
------------------------------------------------------------
ECAT
Comparison Engine
Build : 1.2.3
------------------------------------------------------------
Adds month-to-month difference columns.
------------------------------------------------------------
"""

import pandas as pd


class ComparisonEngine:

    def add_difference_columns(self, df):

        if df.empty:
            return df

        result = pd.DataFrame()

        # First column (Feeder / Location Code)
        result[df.columns[0]] = df.iloc[:, 0]

        # Numeric month columns
        month_columns = list(df.columns[1:])

        if len(month_columns) == 1:
            result[month_columns[0]] = df[month_columns[0]]
            return result

        # First month
        result[month_columns[0]] = df[month_columns[0]]

        # Remaining months + Difference
        for i in range(1, len(month_columns)):

            current = month_columns[i]
            previous = month_columns[i - 1]

            result[current] = df[current]

            result[f"Δ {current}"] = (
                df[current] - df[previous]
            )

        return result