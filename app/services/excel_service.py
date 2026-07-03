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
        # Cache: full file path -> workbook data
        self.cache = {}

    # --------------------------------------------------

    def load_file(self, file_path):
        """
        Read Excel file once and cache results.
        """

        file_path = Path(file_path)
        key = str(file_path)

        if key in self.cache:
            return self.cache[key]

        workbook = pd.ExcelFile(file_path)

        sheets = []

        file_size = round(file_path.stat().st_size / 1024, 2)

        for sheet in workbook.sheet_names:

            df = pd.read_excel(file_path, sheet_name=sheet)

            sheets.append({
                "sheet_name": sheet,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns)
            })

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
        Returns metadata for Treeview display.
        """

        workbook = self.load_file(file_path)

        info = []

        for sheet in workbook["sheets"]:
            info.append({
                "file_name": workbook["file_name"],
                "sheet_name": sheet["sheet_name"],
                "rows": sheet["rows"],
                "columns": sheet["columns"],
                "size_kb": workbook["size_kb"],
                "status": "OK"
            })

        return info

    # --------------------------------------------------

    def get_columns(self, file_path, sheet_name=None):
        """
        Return column names from a sheet.
        Default = first sheet.
        """

        workbook = self.load_file(file_path)

        if not workbook["sheets"]:
            return []

        if sheet_name is None:
            return workbook["sheets"][0]["column_names"]

        for sheet in workbook["sheets"]:
            if sheet["sheet_name"] == sheet_name:
                return sheet["column_names"]

        return []

    # --------------------------------------------------

    def get_common_columns(self, file_list):
        """
        Find common columns across all files.
        """

        if not file_list:
            return []

        common = None

        for file in file_list:
            cols = set(self.get_columns(file))

            if common is None:
                common = cols
            else:
                common &= cols

        if not common:
            return []

        return sorted(list(common))

    # --------------------------------------------------

    def clear_cache(self):
        self.cache.clear()