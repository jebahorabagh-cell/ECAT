import tkinter as tk
from tkinter import ttk

from app.services.dataset_cache import DatasetCache
from app.services.comparison_engine import ComparisonEngine
from app.gui.report_preview import ReportPreview
from app.gui.widgets.multiselect_dropdown import MultiSelectDropdown


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

        ttk.Label(

            top,

            text="Datasets"

        ).grid(

            row=0,

            column=0,

            sticky="w"

        )

        self.dataset_selector = MultiSelectDropdown(top)

        self.dataset_selector.grid(

            row=1,

            column=0,

            columnspan=2,

            sticky="w",

            pady=5
        )

        self.dataset_selector.grid(

            row=1,

            column=0,

            columnspan=2,

            pady=5,

            sticky="w"

        )

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

        self.dataset_selector.set_items(datasets)
        
    
    # --------------------------------------------------

    def compare(self):

        datasets = self.dataset_selector.get_selected()

        if len(datasets) < 2:

            from tkinter import messagebox

            messagebox.showwarning(

                "Comparison",

                "Please select at least two datasets."

            )

            return
            
        print(datasets)

        #old_df = self.cache.load_dataset(dataset_a)

        #new_df = self.cache.load_dataset(dataset_b)

        #result = self.engine.compare_datasets(

        #    old_df,

        #    new_df

       # )

        #self.preview.show_report(result)