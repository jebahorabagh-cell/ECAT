"""
------------------------------------------------------------
ECAT - Excel Comparison & Audit Tool
Build : 1.0.4

Module : Files Page
------------------------------------------------------------
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from app.services.file_manager import FileManager
from app.services.excel_service import ExcelService


class FilesPage(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.file_manager = FileManager()
        self.excel_service = ExcelService()
        self.common_columns = []
        self.selected_column = tk.StringVar()

        self._create_widgets()

    # --------------------------------------------------

    def _create_widgets(self):

        title = tk.Label(
            self,
            text="Loaded Excel Files",
            font=("Segoe UI", 14, "bold")
        )

        title.pack(anchor="w", padx=10, pady=(10, 5))
        
        comparison_frame = tk.Frame(self)

        comparison_frame.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        tk.Label(
            comparison_frame,
            text="Comparison Column:",
            font=("Segoe UI", 10, "bold")
        ).pack(side="left")

        self.column_combo = ttk.Combobox(
            comparison_frame,
            textvariable=self.selected_column,
            state="readonly",
            width=40
        )

        self.column_combo.pack(
            side="left",
            padx=10
        )

        self.tree = ttk.Treeview(
            self,
            columns=(
                "file",
                "sheet",
                "rows",
                "columns",
                "size",
                "status"
            ),
            show="headings",
            height=18
        )

        headings = {
            "file": "File Name",
            "sheet": "Sheet",
            "rows": "Rows",
            "columns": "Columns",
            "size": "Size (KB)",
            "status": "Status"
        }

        widths = {
            "file": 250,
            "sheet": 180,
            "rows": 80,
            "columns": 80,
            "size": 90,
            "status": 250
        }

        for column in headings:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="center")

        self.tree.column("file", anchor="w")
        self.tree.column("sheet", anchor="w")
        self.tree.column("status", anchor="w")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10
        )

        button_frame = tk.Frame(self)

        button_frame.pack(fill="x", padx=10, pady=10)

        tk.Button(
            button_frame,
            text="Add Files",
            width=18,
            command=self.add_files
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Remove Selected",
            width=18,
            command=self.remove_selected
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Clear All",
            width=18,
            command=self.clear_all
        ).pack(side="left", padx=5)

    # --------------------------------------------------

    def add_files(self):

        files = filedialog.askopenfilenames(
            title="Select Excel Files",
            filetypes=[
                ("Excel Files", "*.xlsx *.xls *.xlsm")
            ]
        )

        if not files:
            return

        self.file_manager.add_files(files)

        self.refresh()

    # --------------------------------------------------

    def remove_selected(self):

        selected = self.tree.selection()

        if not selected:
            return

        index = self.tree.index(selected[0])

        self.file_manager.remove(index)

        self.refresh()

    # --------------------------------------------------

    def clear_all(self):

        self.file_manager.clear()

        self.refresh()

    # --------------------------------------------------

    def refresh(self):

        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.common_columns = self.excel_service.get_common_columns(
            self.file_manager.files()
        )

        self.column_combo["values"] = self.common_columns

        if len(self.common_columns) == 1:
            self.column_combo.current(0)

        elif len(self.common_columns) > 1:
            self.column_combo.current(0)

        else:
            self.column_combo.set("")

        for file_path in self.file_manager.files():

            information = self.excel_service.get_file_information(file_path)

            for item in information:

                self.tree.insert(
                    "",
                    tk.END,
                    values=(
                        item["file_name"],
                        item["sheet_name"],
                        item["rows"],
                        item["columns"],
                        item["size_kb"],
                        item["status"]
                    )
                )