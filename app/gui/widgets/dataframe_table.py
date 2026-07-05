import tkinter as tk
from tkinter import ttk


class DataFrameTable(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.tree = ttk.Treeview(self, show="headings")

        vsb = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        hsb = ttk.Scrollbar(
            self,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # -----------------------------------------------------

    def clear(self):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = ()

    # -----------------------------------------------------

    def show(self, dataframe):

        self.clear()

        if dataframe is None:
            return

        columns = list(dataframe.columns)

        self.tree["columns"] = columns

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=140,
                anchor="center"
            )

        for row in dataframe.itertuples(index=False):

            self.tree.insert(
                "",
                "end",
                values=list(row)
            )