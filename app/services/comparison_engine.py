"""
------------------------------------------------------------
ECAT
Comparison Engine
Build : 1.3.2-a
------------------------------------------------------------

Functions
---------
1. Add month-to-month difference columns
2. Compare two billing datasets

------------------------------------------------------------
"""

import pandas as pd
from app.config import business_rules


class ComparisonEngine:

    # =====================================================
    # REPORT COMPARISON
    # =====================================================

    def add_difference_columns(self, df):

        if df.empty:
            return df

        result = pd.DataFrame()

        # First column (Feeder / Location Code)

        result[df.columns[0]] = df.iloc[:, 0]

        month_columns = list(df.columns[1:])

        if len(month_columns) == 1:

            result[month_columns[0]] = df[month_columns[0]]

            return result

        result[month_columns[0]] = df[month_columns[0]]

        for i in range(1, len(month_columns)):

            current = month_columns[i]

            previous = month_columns[i - 1]

            result[current] = df[current]

            result[f"Δ {current}"] = (

                df[current] - df[previous]

            )

        return result

    # =====================================================
    # DATASET COMPARISON
    # =====================================================

    
    
    def compare_datasets(
        self,
        old_df,
        new_df,
        key_column=business_rules.DEFAULT_KEY_COLUMN,
        compare_columns=None
    ):

        if old_df.empty or new_df.empty:

            return pd.DataFrame()

        # ------------------------------------------
        # Common Columns
        # ------------------------------------------

        if compare_columns is None:

            compare_columns = [

                col

                for col in old_df.columns

                if col in new_df.columns

                and col != key_column

            ]

        # ------------------------------------------
        # Merge
        # ------------------------------------------

        merged = old_df.merge(

            new_df,

            on=key_column,

            how="outer",

            suffixes=("_Old", "_New"),

            indicator=True

        )

        # ------------------------------------------
        # Record Status
        # ------------------------------------------

        merged["Record_Status"] = merged["_merge"].map({

            "left_only": "REMOVED",

            "right_only": "ADDED",

            "both": "UNCHANGED"

        })

        # ------------------------------------------
        # Compare Columns
        # ------------------------------------------

        changed_columns = []

        for column in compare_columns:

            old = f"{column}_Old"

            new = f"{column}_New"

            if old not in merged.columns:

                continue

            if new not in merged.columns:

                continue

            changed = f"{column}_Changed"

            merged[changed] = (

                merged[old].fillna("")

                !=

                merged[new].fillna("")

            )

            changed_columns.append(changed)

        # ------------------------------------------
        # Modified Records
        # ------------------------------------------

        if changed_columns:

            modified = merged[changed_columns].any(axis=1)

            merged.loc[

                (merged["Record_Status"] == "UNCHANGED")

                &

                modified,

                "Record_Status"

            ] = "MODIFIED"

        # ------------------------------------------
        # Column Order
        # ------------------------------------------

        columns = [

            key_column,

            "Record_Status"

        ]

        for column in compare_columns:

            old = f"{column}_Old"

            new = f"{column}_New"

            changed = f"{column}_Changed"

            if old in merged.columns:

                columns.append(old)

            if new in merged.columns:

                columns.append(new)

            if changed in merged.columns:

                columns.append(changed)

        return merged[columns].reset_index(drop=True)