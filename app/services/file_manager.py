"""
------------------------------------------------------------
ECAT - Excel Comparison & Audit Tool
Build : 1.0.3

Module : File Manager

Purpose
-------
Stores the list of Excel files selected by the user.

NOTE
----
This class DOES NOT read Excel files.
It only manages the file list.
------------------------------------------------------------
"""

from pathlib import Path


class FileManager:
    """Manage selected Excel files."""

    VALID_EXTENSIONS = {".xlsx", ".xls", ".xlsm"}

    def __init__(self):
        self._files = []

    # --------------------------------------------------
    # Public Methods
    # --------------------------------------------------

    def add_files(self, file_paths):
        """
        Add one or more files.

        Duplicate files are ignored.
        Non-excel files are ignored.
        """

        for file in file_paths:

            path = Path(file)

            if not path.exists():
                continue

            if path.suffix.lower() not in self.VALID_EXTENSIONS:
                continue

            if path not in self._files:
                self._files.append(path)

    def remove(self, index):
        """Remove file by index."""

        if 0 <= index < len(self._files):
            self._files.pop(index)

    def clear(self):
        """Remove all files."""

        self._files.clear()

    # --------------------------------------------------
    # Getters
    # --------------------------------------------------

    def files(self):
        """Return copy of file list."""

        return self._files.copy()

    def count(self):
        """Return total number of files."""

        return len(self._files)

    def file_name(self, index):
        """Return filename only."""

        return self._files[index].name

    def full_path(self, index):
        """Return complete path."""

        return str(self._files[index])

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def is_empty(self):
        return len(self._files) == 0

    def contains(self, path):
        return Path(path) in self._files

    def __len__(self):
        return len(self._files)

    def __iter__(self):
        return iter(self._files)