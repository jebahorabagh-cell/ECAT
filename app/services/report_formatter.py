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

        if df.empty:
            return df

        df = self._replace_feeder_names(df)

        df = self._sort_feeders(df)
    
        df = self._rename_first_column(df)

        df = self._format_numeric_columns(df)

        return df
    # --------------------------------------------------
    
    def _clean_column_names(self, df):

        columns = []

        for column in df.columns:

            columns.append(
                str(column).strip()
            )

        df.columns = columns

        return df
    #----------------------------------------------------    
    

    def _replace_feeder_names(self, df):

        location_column = df.columns[0]

        def convert(value):

            try:
                return business_rules.feeder_name(int(value))
            except (ValueError, TypeError):
                # Already a summary label like "ZONE 1 SUMMARY"
                return value

        df[location_column] = df[location_column].apply(convert)

        return df

    # --------------------------------------------------

    def _sort_feeders(self, df):

        feeder_order = [
            business_rules.feeder_name(code)
            for code in business_rules.feeder_sequence()
        ]
        
        feeder_order.extend([
            "ZONE 1 SUMMARY",
            "ZONE 2 SUMMARY",
            "DIVISION SUMMARY"
        ])

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
    #--------------------------------------------------------
        
    def _rename_first_column(self, df):

        first_column = df.columns[0]

        df = df.rename(
            columns={
                first_column: "Feeder"
            }
        )

        return df
    #--------------------------------------------------------
        
    def _format_numeric_columns(self, df):

        numeric_columns = df.columns[1:]

        df[numeric_columns] = (
            df[numeric_columns]
            .round(2)
        )

        return df