"""
------------------------------------------------------------
ECAT
Summary Comparison Engine
Build : 1.4.1
------------------------------------------------------------
Creates feeder-wise comparison reports across
multiple datasets.
------------------------------------------------------------
"""

import pandas as pd

from app.services.data_loader import DataLoader
from app.services.aggregation_engine import AggregationEngine


class SummaryComparisonEngine:

    def __init__(self):

        self.loader = DataLoader()

        self.aggregator = AggregationEngine()

    # --------------------------------------------------

    def generate(

        self,

        datasets,

        compare_column,

        aggregation="sum"

    ):

        report = None

        for dataset in datasets:

            df = self.loader.load_datasets([dataset])

            grouped = (

                df.groupby("Location Code")[compare_column]

                .agg(aggregation)

                .reset_index()

            )

            grouped.rename(

                columns={

                    compare_column: dataset

                },

                inplace=True

            )

            if report is None:

                report = grouped

            else:

                report = report.merge(

                    grouped,

                    on="Location Code",

                    how="outer"

                )

        return report.fillna(0)