import tkinter as tk
from tkinter import ttk

from app.services.dataset_cache import DatasetCache
from app.services.comparison_engine import ComparisonEngine
from app.gui.report_preview import ReportPreview


class ComparisonPage(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.cache = DatasetCache()
        self.engine = ComparisonEngine()

        self.build_ui()

    # --------------------------------------------------

    def build_ui(self):

        title = ttk.Label(

            self,

            text="Dataset Comparison",

            font=("Segoe UI", 16, "bold")

        )

        title.pack(anchor="w", padx=10, pady=10)

        top = ttk.Frame(self)

        top.pack(fill="x", padx=10)

        ttk.Label(top, text="Dataset A").grid(row=0, column=0)

        self.dataset_a = ttk.Combobox(top, state="readonly", width=30)

        self.dataset_a.grid(row=0, column=1, padx=5)

        ttk.Label(top, text="Dataset B").grid(row=0, column=2)

        self.dataset_b = ttk.Combobox(top, state="readonly", width=30)

        self.dataset_b.grid(row=0, column=3, padx=5)

        ttk.Button(

            top,

            text="Compare",

            command=self.compare

        ).grid(row=0, column=4, padx=10)

        self.preview = ReportPreview(self)

        self.preview.pack(fill="both", expand=True)

        self.load_datasets()

    # --------------------------------------------------

    def load_datasets(self):

        datasets = [

            d["dataset_name"]

            for d in self.cache.available_datasets()

        ]

        self.dataset_a["values"] = datasets

        self.dataset_b["values"] = datasets
        
    # --------------------------------------------------

    # --------------------------------------------------

    def compare(self):

        dataset_a = self.dataset_a.get()

        dataset_b = self.dataset_b.get()

        if not dataset_a or not dataset_b:

            from tkinter import messagebox

            messagebox.showwarning(

                "Comparison",

                "Please select both datasets."

            )

            return

        old_df = self.cache.load_dataset(dataset_a)

        new_df = self.cache.load_dataset(dataset_b)

        result = self.engine.compare_datasets(

            old_df,

            new_df

        )

        self.preview.show_report(result)