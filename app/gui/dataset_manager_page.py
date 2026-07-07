import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from pathlib import Path


class DatasetManagerPage(ttk.Frame):

    def __init__(self, parent, dataset_manager):

        super().__init__(parent)

        self.dataset_manager = dataset_manager

        self.build_ui()

        self.refresh()

    # --------------------------------------------------

    def build_ui(self):

        title = ttk.Label(

            self,

            text="Dataset Manager",

            font=("Segoe UI", 16, "bold")

        )

        title.pack(
            anchor="w",
            padx=10,
            pady=(10, 15)
        )

        body = ttk.Frame(self)

        body.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ----------------------------

        left = ttk.Frame(body)

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        ttk.Label(

            left,

            text="Imported Datasets"

        ).pack(anchor="w")

        self.listbox = tk.Listbox(

            left,

            height=20,

            font=("Segoe UI", 10)

        )

        self.listbox.pack(
            fill="both",
            expand=True,
            pady=5
        )

        # ----------------------------

        right = ttk.Frame(body)

        right.pack(
            side="left",
            fill="y",
            padx=15
        )

        ttk.Button(

            right,

            text="Import Dataset",

            width=20,

            command=self.import_dataset

        ).pack(
            pady=5
        )

        ttk.Button(

            right,

            text="Refresh Dataset",

            width=20,

            command=self.refresh_dataset

        ).pack(
            pady=5
        )

        ttk.Button(

            right,

            text="Delete Dataset",

            width=20,

            command=self.delete_dataset

        ).pack(
            pady=5
        )

    # --------------------------------------------------

    def refresh(self):

        self.listbox.delete(0, tk.END)

        for name in self.dataset_manager.dataset_names():

            self.listbox.insert(tk.END, name)

    # --------------------------------------------------

    def import_dataset(self):

        file = filedialog.askopenfilename(

            title="Select Dataset",

            filetypes=[

                ("Excel Files", "*.xlsx *.xls")

            ]

        )

        if not file:

            return

        dataset_name = Path(file).stem

        if self.dataset_manager.exists(dataset_name):

            messagebox.showinfo(

                "ECAT",

                f"{dataset_name} already exists."

            )

            return

        self.dataset_manager.import_dataset(file)

        self.refresh()

        messagebox.showinfo(

            "ECAT",

            "Dataset imported successfully."

        )

    # --------------------------------------------------

    def refresh_dataset(self):

        print("Refresh Dataset")

    # --------------------------------------------------

    def delete_dataset(self):

        print("Delete Dataset")