"""
------------------------------------------------------------
ECAT
Report
Build 1.0.10
------------------------------------------------------------
"""


class Report:

    def __init__(self):

        self.title = "Untitled Report"

        self.blocks = []

    # --------------------------------------------------

    def set_title(self, title):

        self.title = title

    # --------------------------------------------------

    def add_block(self, report_definition):

        self.blocks.append(report_definition)

    # --------------------------------------------------

    def remove_block(self, index):

        if 0 <= index < len(self.blocks):

            self.blocks.pop(index)

    # --------------------------------------------------

    def clear(self):

        self.blocks.clear()

    # --------------------------------------------------

    def count(self):

        return len(self.blocks)

    # --------------------------------------------------

    def all_blocks(self):

        return self.blocks