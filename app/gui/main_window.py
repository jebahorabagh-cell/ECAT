"""
ECAT - Main Window
Build 1.0.3
"""

import tkinter as tk

from app.gui.files_page import FilesPage


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("ECAT - Excel Comparison & Audit Tool")

        self.root.geometry("1100x700")

        self.root.minsize(900, 600)

        self._create_menu()

        self._create_layout()

    # -------------------------------------------------

    def _create_menu(self):

        menu = tk.Menu(self.root)

        for title in ("File", "Project", "Settings", "Help"):

            submenu = tk.Menu(menu, tearoff=False)

            submenu.add_command(label="Coming Soon")

            menu.add_cascade(label=title, menu=submenu)

        self.root.config(menu=menu)

    # -------------------------------------------------

    def _create_layout(self):

        self.root.grid_rowconfigure(0, weight=1)

        self.root.grid_columnconfigure(1, weight=1)

        # ---------------- Navigation ----------------

        navigation = tk.Frame(
            self.root,
            width=180,
            bd=1,
            relief="solid"
        )

        navigation.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        navigation.grid_propagate(False)

        tk.Button(
            navigation,
            text="Files",
            width=18
        ).pack(
            padx=10,
            pady=(15, 5)
        )

        # Placeholders for future modules

        for item in (
            "Compare",
            "Reports",
            "Settings"
        ):

            tk.Button(
                navigation,
                text=item,
                width=18,
                state="disabled"
            ).pack(
                padx=10,
                pady=5
            )

        # ---------------- Workspace ----------------

        workspace = tk.Frame(
            self.root,
            bd=1,
            relief="solid"
        )

        workspace.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        workspace.grid_rowconfigure(0, weight=1)
        workspace.grid_columnconfigure(0, weight=1)

        self.files_page = FilesPage(workspace)

        self.files_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ---------------- Status ----------------

        self.status = tk.Label(
            self.root,
            text="Ready",
            anchor="w",
            bd=1,
            relief="sunken"
        )

        self.status.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew"
        )

    # -------------------------------------------------

    def run(self):

        self.root.mainloop()