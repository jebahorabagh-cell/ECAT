"""
------------------------------------------------------------
ECAT - Excel Comparison & Audit Tool
Build : 1.0.5

Excel Service

Purpose
-------
1. Read Excel metadata
2. Read column names
3. Cache workbook information
4. Find common columns
------------------------------------------------------------
"""

from pathlib import Path

import pandas as pd


class ExcelService:

    def __init__(self):

        # Cache
        # Key = full file path
        # Value = metadata dictionary
        self.cache = {}

    # --------------------------------------------------

    def load_file(self, file_path):

        """
        Read an Excel file only once and
        store everything required for future use.
        """

        file_path = Path(file_path)

        key = str(file_path)

        if key in self.cache:
            return self.cache[key]

        workbook = pd.ExcelFile(file_path)

        sheets = []

        file_size = round(
            file_path.stat().st_size / 1024,
            2
        )

        for sheet in workbook.sheet_names:

            df = pd.read_excel(
                file_path,
                sheet_name=sheet
            )

            sheets.append(
                {
                    "sheet_name": sheet,
                    "rows": len(df),
                    "columns": len(df.columns),
                    "column_names": list(df.columns)
                }
            )

        data = {
            "file_name": file_path.name,
            "full_path": key,
            "size_kb": file_size,
            "sheets": sheets
        }

        self.cache[key] = data

        return data

    # --------------------------------------------------

    def get_file_information(self, file_path):

        """
        Returns metadata for display in Treeview.
        """

        workbook = self.load_file(file_path)

        information = []

        for sheet in workbook["sheets"]:

            information.append(
                {
                    "file_name": workbook["file_name"],
                    "sheet_name": sheet["sheet_name"],
                    "rows": sheet["rows"],
                    "columns": sheet["columns"],
                    "size_kb": workbook["size_kb"],
                    "status": "OK"
                }
            )

        return information

    # --------------------------------------------------

    def get_columns(self, file_path):

        """
        Return all columns from first worksheet.
        """

        workbook = self.load_file(file_path)

        if not workbook["sheets"]:
            return []

        return workbook["sheets"][0]["column_names"]

    # --------------------------------------------------

    def get_common_columns(self, file_list):

        """
        Find common columns among all loaded files.
        """

        if not file_list:
            return []

        common = set(
            self.get_columns(file_list[0])
        )

        for file in file_list[1:]:

            common &= set(
                self.get_columns(file)
            )

        return sorted(common)

    # --------------------------------------------------

    def clear_cache(self):

        self.cache.clear()