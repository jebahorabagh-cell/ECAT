"""
------------------------------------------------------------
ECAT - Excel Comparison & Audit Tool
Dataset Manager
Build : 1.0.6
------------------------------------------------------------
"""


class DatasetManager:
    """
    Maintains all loaded datasets.

    Every loaded Excel file becomes one dataset.
    """

    def __init__(self):

        self.datasets = []

    # --------------------------------------------------

    def clear(self):

        self.datasets.clear()

    # --------------------------------------------------

    def add_dataset(
        self,
        label,
        dataframe,
        file_path
    ):

        dataset = {
            "label": label,
            "dataframe": dataframe,
            "file_path": file_path
        }

        self.datasets.append(dataset)

    # --------------------------------------------------

    def count(self):

        return len(self.datasets)

    # --------------------------------------------------

    def labels(self):

        return [
            d["label"]
            for d in self.datasets
        ]

    # --------------------------------------------------

    def get(self, label):

        for dataset in self.datasets:

            if dataset["label"] == label:
                return dataset

        return None

    # --------------------------------------------------

    def all(self):

        return self.datasets