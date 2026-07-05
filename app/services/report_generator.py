"""
------------------------------------------------------------
ECAT
Report Generator
Build : 1.2.2
------------------------------------------------------------
"""

from app.services.data_loader import DataLoader
from app.services.filter_engine import FilterEngine
from app.services.aggregation_engine import AggregationEngine
from app.services.report_formatter import ReportFormatter


class ReportGenerator:

    def __init__(self):

        self.loader = DataLoader()

        self.filter_engine = FilterEngine()

        self.aggregation_engine = AggregationEngine()

        self.formatter = ReportFormatter()

    # ----------------------------------------------------

    def generate(self, files, request):

        # Load all selected files
        df = self.loader.load(files)

        # Apply filters
        df = self.filter_engine.apply(df, request)

        # Create pivot report
        df = self.aggregation_engine.aggregate(df, request)

        # Apply business formatting
        df = self.formatter.format(df)

        return df