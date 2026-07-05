"""
------------------------------------------------------------
ECAT - Report Definition
Build : 1.0.7
------------------------------------------------------------
"""


class ReportDefinition:

    def __init__(self):

        self.title = ""

        self.rows = []

        self.columns = []

        self.values = []

        self.filters = {}

        self.calculations = []

        self.sort_by = None

        self.sort_order = "ascending"

    # --------------------------------------------------

    def set_title(self, title):
        self.title = title

    # --------------------------------------------------

    def add_row(self, column):
        self.rows.append(column)

    # --------------------------------------------------

    def add_column(self, column):
        self.columns.append(column)

    # --------------------------------------------------

    def add_value(
        self,
        column,
        aggregation
    ):

        self.values.append(
            {
                "column": column,
                "aggregation": aggregation
            }
        )

    # --------------------------------------------------

    def add_filter(
        self,
        column,
        value
    ):

        self.filters[column] = value

    # --------------------------------------------------

    def add_calculation(
        self,
        calculation
    ):

        self.calculations.append(calculation)