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
from app.services.summary_engine import SummaryEngine
from app.services.comparison_engine import ComparisonEngine
from app.services.excel_exporter import ExcelExporter

class ReportGenerator:

    def __init__(self):

        self.loader = DataLoader()

        self.filter_engine = FilterEngine()

        self.aggregation_engine = AggregationEngine()

        self.formatter = ReportFormatter()
        
        self.summary_engine = SummaryEngine()
        
        self.comparison_engine = ComparisonEngine()
        
        self.exporter = ExcelExporter()
        self.current_report = None

    # ----------------------------------------------------

    def generate(self, files, request):

        # Load all selected files
        df = self.loader.load(files)

        # Apply filters
        df = self.filter_engine.apply(df, request)

        # Create pivot report
        df = self.aggregation_engine.aggregate(df, request)
        
        df = self.summary_engine.add_summaries(df)
        
        if request.get("difference", True):
            df = self.comparison_engine.add_difference_columns(df)

        # Apply business formatting
        df = self.formatter.format(df)

        return df