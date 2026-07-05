"""
------------------------------------------------------------
ECAT
Universal Report Generator
Build : 1.1.4
------------------------------------------------------------
"""

import pandas as pd

from app.analytics.report_formatter import ReportFormatter


class ReportGenerator:

    def __init__(self):

        self.formatter = ReportFormatter()

    # ---------------------------------------------------------

    def _apply_filters(self, df, filters):

        """
        Apply all filters to dataframe.

        Example

        filters = {

            "Consumer Status":"ACTIVE",

            "Tariff Category":"LV3"

        }

        """

        if not filters:
            return df

        for column, value in filters.items():

            if column not in df.columns:
                continue

            df = df[
                df[column]
                .astype(str)
                .str.upper()
                ==
                str(value).upper()
            ]

        return df

    # ---------------------------------------------------------

    def _aggregate(
        self,
        df,
        group_by,
        value,
        aggregation
    ):

        if aggregation.lower() == "sum":

            return (
                df
                .groupby(group_by)[value]
                .sum()
                .reset_index()
            )

        elif aggregation.lower() == "count":

            return (
                df
                .groupby(group_by)[value]
                .count()
                .reset_index()
            )

        elif aggregation.lower() == "mean":

            return (
                df
                .groupby(group_by)[value]
                .mean()
                .reset_index()
            )

        elif aggregation.lower() == "max":

            return (
                df
                .groupby(group_by)[value]
                .max()
                .reset_index()
            )

        elif aggregation.lower() == "min":

            return (
                df
                .groupby(group_by)[value]
                .min()
                .reset_index()
            )

        else:

            raise ValueError(
                f"Unsupported aggregation : {aggregation}"
            )

    # ---------------------------------------------------------

    def generate(

        self,

        dataset_manager,

        group_by,

        value,

        aggregation="sum",

        filters=None,

        difference=True

    ):

        """
        Universal Report Generator
        """

        report = None

        for dataset in dataset_manager.all():

            label = dataset["label"]

            df = dataset["dataframe"].copy()

            df = self._apply_filters(
                df,
                filters
            )

            grouped = self._aggregate(
                df,
                group_by,
                value,
                aggregation
            )

            grouped.rename(

                columns={

                    value: label

                },

                inplace=True

            )

            if report is None:

                report = grouped

            else:

                report = report.merge(

                    grouped,

                    on=group_by,

                    how="outer"

                )

        if report is None:

            return pd.DataFrame()

        report.fillna(0, inplace=True)

        # ----------------------------------------

        if difference:

            month_columns = [

                c

                for c in report.columns

                if c != group_by

            ]

            for i in range(

                1,

                len(month_columns)

            ):

                current = month_columns[i]

                previous = month_columns[i-1]

                report[
                    f"Diff {current}"
                ] = (

                    report[current]

                    -

                    report[previous]

                )

        # ----------------------------------------

        if group_by == "Location Code":

            report = self.formatter.format(
                report
            )

        return report