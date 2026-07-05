"""
------------------------------------------------------------
ECAT
Report Generator
Build : 1.2.0
Phase A
------------------------------------------------------------
"""


from app.services.data_loader import DataLoader
from app.services.filter_engine import FilterEngine
from app.services.aggregation_engine import AggregationEngine


class ReportGenerator:

    def __init__(self):

        self.loader = DataLoader()
        
        self.filter_engine = FilterEngine()
        
        self.aggregation_engine = AggregationEngine()

    # ----------------------------------------------------

    def generate(self, files, request):

        df = self.loader.load(files)
        
        df = self.filter_engine.apply(
            df,
            request
        )

        print("\n========== DATA LOADER ==========")

        print(f"Rows    : {len(df)}")
        print(f"Columns : {len(df.columns)}")

        print("\nColumns Found:")

        for column in df.columns:
            print("•", column)

        print("\nFirst 5 Rows:\n")

        print(df.head())

        print("\n=================================")

        df = self.aggregation_engine.aggregate(
            df,
            request
        )

        return df