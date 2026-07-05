"""
------------------------------------------------------------
ECAT
Aggregation Engine
Build : 1.2.1
------------------------------------------------------------
"""

import pandas as pd


class AggregationEngine:

    def aggregate(self, df, request):

        print("\n========== AGGREGATION ENGINE ==========")

        if df.empty:
            print("No data available.")
            return pd.DataFrame()

        group_column = request["group_by"]
        value_column = request["value"]
        aggregation = request["aggregation"]

        print(f"Group By    : {group_column}")
        print(f"Value       : {value_column}")
        print(f"Aggregation : {aggregation}")

        # --------------------------------------------
        # Group
        # --------------------------------------------

        result = (

            df

            .groupby(
                [
                    group_column,
                    "Dataset"
                ]
            )[value_column]

            .agg(aggregation)

            .reset_index()

        )

        print(f"\nGrouped Rows : {len(result)}")

        # --------------------------------------------
        # Pivot
        # --------------------------------------------

        pivot = result.pivot(

            index=group_column,

            columns="Dataset",

            values=value_column

        )

        pivot = pivot.fillna(0)

        pivot = pivot.reset_index()

        print("\nPivot Preview\n")

        print(pivot.head())

        print("\n========================================")

        return pivot