"""
------------------------------------------------------------
ECAT
Multi Select Dropdown
Build : 1.4.2
------------------------------------------------------------
Reusable multi-selection dropdown widget.
------------------------------------------------------------
"""

import tkinter as tk
from tkinter import ttk


class MultiSelectDropdown(ttk.Frame):

    def __init__(self, parent, width=35):

        super().__init__(parent)

        self.items = []
        self.variables = {}

        self.text = tk.StringVar(value="Select Datasets")

        self.button = ttk.Button(

            self,

            textvariable=self.text,

            command=self.show_popup,

            width=width

        )

        self.button.pack(fill="x")

    # --------------------------------------------------

    def set_items(self, items):

        self.items = list(items)

        new_variables = {}

        for item in items:

            if item in self.variables:

                new_variables[item] = self.variables[item]

            else:

                new_variables[item] = tk.BooleanVar()

        self.variables = new_variables

        self.items = list(items)

        self.text.set("Select Datasets")

    # --------------------------------------------------

    def show_popup(self):

        popup = tk.Toplevel(self)

        popup.title("Select")

        popup.transient(self.winfo_toplevel())

        popup.grab_set()

        frame = ttk.Frame(popup)

        frame.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=10

        )

        

        for item in self.items:

            var = self.variables[item]

            ttk.Checkbutton(

                frame,

                text=item,

                variable=var

            ).pack(anchor="w")

        ttk.Separator(frame).pack(

            fill="x",

            pady=8

        )

        ttk.Button(

            frame,

            text="OK",

            command=lambda: self.finish_selection(popup)

        ).pack()

    # --------------------------------------------------

    def finish_selection(self, popup):

        popup.destroy()

        selected = self.get_selected()

        if selected:

            self.text.set(

                ", ".join(selected)

            )

        else:

            self.text.set(

                "Select Datasets"

            )

    # --------------------------------------------------

    def get_selected(self):

        return [

            item

            for item, var in self.variables.items()

            if var.get()

        ]

    # --------------------------------------------------

    def clear(self):

        for var in self.variables.values():

            var.set(False)

        self.text.set("Select Datasets")