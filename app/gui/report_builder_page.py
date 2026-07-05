import tkinter as tk
from tkinter import ttk

from app.gui.widgets.labeled_combobox import LabeledCombobox
from app.services.report_generator import ReportGenerator
from app.gui.report_preview import ReportPreview
from app.services.excel_exporter import ExcelExporter

class ReportBuilderPage(ttk.Frame):

    def __init__(
        self,
        parent,
        file_manager,
        excel_service
    ):

        super().__init__(parent)

        self.file_manager = file_manager
        self.excel_service = excel_service        
        self.report_generator = ReportGenerator()        
        self.exporter = ExcelExporter()
        self.current_report = None
        self.build_ui()

    # ---------------------------------------------------

    def build_ui(self):

        self.columnconfigure(0, weight=1)

        title = ttk.Label(
            self,
            text="Report Builder",
            font=("Segoe UI", 16, "bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=15,
            pady=(10, 20)
        )

        body = ttk.Frame(self)

        body.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=15
        )

        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)

        # ---------------- Left Panel ----------------

        left = ttk.LabelFrame(
            body,
            text="Report Settings"
        )

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.report_name = LabeledCombobox(
            left,
            "Report Type",
            [
                "Feeder Consumption",
                "Feeder Revenue",
                "Consumer Count"
            ]
        )

        self.report_name.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.group_by = LabeledCombobox(
            left,
            "Group By",
            [
                "Location Code",
                "Reader",
                "Tariff Category"
            ]
        )

        self.group_by.pack(
            fill="x",
            padx=10
        )

        self.value = LabeledCombobox(
            left,
            "Value",
            [
                "Total Unit",
                "Net Amount",
                "Consumer No"
            ]
        )

        self.value.pack(
            fill="x",
            padx=10
        )

        self.aggregation = LabeledCombobox(
            left,
            "Aggregation",
            [
                "sum",
                "count",
                "mean",
                "max",
                "min"
            ]
        )

        self.aggregation.pack(
            fill="x",
            padx=10
        )

        # ---------------- Filters ----------------

        filters = ttk.LabelFrame(
            left,
            text="Filters"
        )

        filters.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.status = LabeledCombobox(
            filters,
            "Consumer Status",
            [
                "ACTIVE",
                "INACTIVE"
            ]
        )

        self.status.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.tariff = LabeledCombobox(
            filters,
            "Tariff Category",
            [
                "LV1",
                "LV2",
                "LV3",
                "LV4",
                "HT"
            ]
        )

        self.tariff.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.show_difference = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            left,
            text="Show Month-to-Month Difference",
            variable=self.show_difference
        ).pack(
            anchor="w",
            padx=15,
            pady=10
        )

        # ---------------- Buttons ----------------

        button_frame = ttk.Frame(left)

        button_frame.pack(
            fill="x",
            padx=10,
            pady=15
        )

        ttk.Button(
            button_frame,
            text="Preview Report",
            command=self.preview_report
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            button_frame,
            text="Export Excel",
            command=self.export_excel
        ).pack(
            side="left",
            padx=5
        )

        # ---------------- Right Panel ----------------

        preview = ttk.LabelFrame(
            body,
            text="Preview"
        )

        preview.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        preview.columnconfigure(0, weight=1)
        preview.rowconfigure(0, weight=1)

        self.report_preview = ReportPreview(preview)

        self.report_preview.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        
# ---------------------------------------------------

    def preview_report(self):

        request = {

            "report_type": self.report_name.get(),

            "group_by": self.group_by.get(),

            "value": self.value.get(),

            "aggregation": self.aggregation.get(),

            "status": self.status.get(),

            "tariff": self.tariff.get(),

            "difference": self.show_difference.get()

        }

        report = self.report_generator.generate(

            files=self.file_manager.files(),

            request=request

        )
        
        self.current_report = report

        self.report_preview.show_report(report)
        
    def export_excel(self):

        if self.current_report is None:
            return

        filepath = self.exporter.export(
            self.current_report,
            report_name=self.report_name.get()
        )

        print(f"Report exported to: {filepath}")