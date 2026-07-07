"""
------------------------------------------------------------
ECAT
Data Loader
Build : 1.2.0
------------------------------------------------------------
"""

from pathlib import Path
import pandas as pd
from app.services.dataset_cache import DatasetCache


class DataLoader:

    def load(self, files):

        datasets = []
    
        cache = DatasetCache()

        for file in files:

            df = cache.load_or_create(file)

            dataset_name = Path(file).stem

            df["Dataset"] = dataset_name

            datasets.append(df)

        if not datasets:
            return pd.DataFrame()

        return pd.concat(
            datasets,
            ignore_index=True
        )