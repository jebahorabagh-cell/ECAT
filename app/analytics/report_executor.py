"""
------------------------------------------------------------
ECAT - Report Executor
Build : 1.0.8
------------------------------------------------------------
"""

import pandas as pd


class ReportExecutor:

    def __init__(self, analytics_engine):
        self.analytics = analytics_engine

    # --------------------------------------------------

    def execute(
        self,
        dataset_manager,
        report_definition
    ):
        """
        Execute a report definition on all datasets.

        Returns one merged DataFrame.
        """

        final_result = None

        for dataset in dataset_manager.all():

            label = dataset["label"]

            df = dataset["dataframe"]

            value = report_definition.values[0]

            result = self.analytics.group_by(
                df=df,
                rows=report_definition.rows,
                values=value["column"],
                aggregation=value["aggregation"],
                filters=report_definition.filters
            )

            result = result.rename(
                columns={
                    value["column"]: label
                }
            )

            if final_result is None:

                final_result = result

            else:

                final_result = final_result.merge(
                    result,
                    on=report_definition.rows,
                    how="outer"
                )

        if final_result is None:
            return pd.DataFrame()

        return final_result