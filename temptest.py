from app.exporters.excel_exporter import ExcelExporter

exporter = ExcelExporter()

exporter.export(

    dataframe=report,

    filename="Consumption_Report.xlsx",

    report_title="Feeder Consumption Report",

    period="Apr 2026 vs May 2026",

    filters="Status=Active | Tariff=LV3"

)