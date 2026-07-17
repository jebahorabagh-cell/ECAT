import tkinter as tk

from app.gui.widgets.multiselect_dropdown import MultiSelectDropdown

root = tk.Tk()

dropdown = MultiSelectDropdown(root)

dropdown.pack(padx=20, pady=20)

dropdown.set_items([
    "APR-2026",
    "MAY-2026",
    "JUN-2026",
    "JUL-2026"
])

root.mainloop()