"""
------------------------------------------------------------
ECAT
Data Loader
Build : 1.2.0
------------------------------------------------------------
"""

from pathlib import Path
import pandas as pd


class DataLoader:

    def load(self, files):

        datasets = []

        for file in files:

            df = pd.read_excel(file)

            dataset_name = Path(file).stem

            df["Dataset"] = dataset_name

            datasets.append(df)

        if not datasets:
            return pd.DataFrame()

        return pd.concat(
            datasets,
            ignore_index=True
        )