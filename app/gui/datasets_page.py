import tkinter as tk
from tkinter import ttk

from app.services.dataset_cache import DatasetCache


class DatasetsPage(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.cache = DatasetCache()

        self.build_ui()

        self.load_datasets()

    # --------------------------------------------------

    def build_ui(self):

        title = ttk.Label(
            self,
            text="Dataset Library",
            font=("Segoe UI", 16, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(10, 15)
        )

        columns = (
            "Dataset",
            "Rows",
            "Columns",
            "Imported",
            "Version"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.tree.heading(column, text=column)

            self.tree.column(
                column,
                width=150,
                anchor="center"
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    # --------------------------------------------------

    def load_datasets(self):

        for row in self.tree.get_children():

            self.tree.delete(row)

        for dataset in self.cache.available_datasets():

            self.tree.insert(
                "",
                "end",
                values=(

                    dataset["dataset_name"],

                    dataset["rows"],

                    dataset["columns"],

                    dataset["created"],

                    dataset["ecat_version"]

                )
            )