"""
ECAT - Main Window
Build 1.1.8
"""

import tkinter as tk

from app.gui.files_page import FilesPage
from app.gui.report_builder_page import ReportBuilderPage


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("ECAT - Electricity Consumption Analysis Tool")

        self.root.geometry("1200x750")

        self.root.minsize(1000, 650)

        self.pages = {}

        self._create_menu()
        self._create_layout()

    # -----------------------------------------------------

    def _create_menu(self):

        menu = tk.Menu(self.root)

        for title in ("File", "Project", "Settings", "Help"):

            submenu = tk.Menu(menu, tearoff=False)

            submenu.add_command(label="Coming Soon")

            menu.add_cascade(
                label=title,
                menu=submenu
            )

        self.root.config(menu=menu)

    # -----------------------------------------------------

    def _create_layout(self):

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # =================================================
        # Navigation Panel
        # =================================================

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

        tk.Label(
            navigation,
            text="ECAT",
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=(20, 25)
        )

        tk.Button(

            navigation,

            text="Files",

            width=18,

            command=lambda: self.show_page("files")

        ).pack(
            pady=5
        )

        tk.Button(

            navigation,

            text="Report Builder",

            width=18,

            command=lambda: self.show_page("report_builder")

        ).pack(
            pady=5
        )

        # Disabled (Future)

        for item in (

            "Dashboard",

            "Templates",

            "Settings"

        ):

            tk.Button(

                navigation,

                text=item,

                width=18,

                state="disabled"

            ).pack(
                pady=5
            )

        # =================================================
        # Workspace
        # =================================================

        self.workspace = tk.Frame(
            self.root,
            bd=1,
            relief="solid"
        )

        self.workspace.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.workspace.grid_rowconfigure(0, weight=1)
        self.workspace.grid_columnconfigure(0, weight=1)

        # =================================================
        # Pages
        # =================================================

        self.pages["files"] = FilesPage(
            self.workspace
        )

        self.pages["report_builder"] = ReportBuilderPage(
            self.workspace
        )

        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        

        # =================================================
        # Status Bar
        # =================================================

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
        
        # Show first page LAST
        self.show_page("files")
    # -----------------------------------------------------

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:

            page.tkraise()

            self.status.config(
                text=f"Page : {page_name.replace('_',' ').title()}"
            )

    # -----------------------------------------------------

    def run(self):

        self.root.mainloop()