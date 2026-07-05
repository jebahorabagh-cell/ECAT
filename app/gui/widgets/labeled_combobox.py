import tkinter as tk
from tkinter import ttk


class LabeledCombobox(ttk.Frame):

    def __init__(self, parent, text, values=None, width=30):
        super().__init__(parent)

        if values is None:
            values = []

        self.label = ttk.Label(
            self,
            text=text
        )

        self.combo = ttk.Combobox(
            self,
            values=values,
            width=width,
            state="readonly"
        )

        self.label.pack(
            anchor="w"
        )

        self.combo.pack(
            fill="x",
            pady=(2, 8)
        )

        if values:
            self.combo.current(0)

    def get(self):
        return self.combo.get()

    def set(self, value):
        self.combo.set(value)

    def configure_values(self, values):
        self.combo["values"] = values

        if values:
            self.combo.current(0)