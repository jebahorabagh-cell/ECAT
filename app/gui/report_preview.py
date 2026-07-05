import tkinter as tk

from app.gui.widgets.dataframe_table import DataFrameTable


class ReportPreview(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        title = tk.Label(
            self,
            text="Report Preview",
            font=("Segoe UI", 16, "bold")
        )

        title.pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        self.table = DataFrameTable(self)

        self.table.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # -------------------------------------------------

    def show_report(self, dataframe):
        self.table.show(dataframe)