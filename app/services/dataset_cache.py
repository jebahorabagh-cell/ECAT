"""
------------------------------------------------------------
ECAT
Dataset Cache
Build : 1.3.0
------------------------------------------------------------
Creates and maintains cached parquet datasets.
------------------------------------------------------------
"""

from pathlib import Path
import json
from datetime import datetime
import pandas as pd

class DatasetCache:

    def __init__(self):

        self.dataset_folder = Path("datasets")

        self.dataset_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    # --------------------------------------------------

    def cache_path(self, excel_path):

        excel_path = Path(excel_path)

        return self.dataset_folder / (
            excel_path.stem + ".parquet"
        )

    # --------------------------------------------------

    def is_cache_valid(self, excel_path):

        excel_path = Path(excel_path)

        cache = self.cache_path(excel_path)

        # Cache doesn't exist
        if not cache.exists():
            return False

        excel_time = excel_path.stat().st_mtime
        cache_time = cache.stat().st_mtime

        # Cache is newer than Excel
        return cache_time >= excel_time

    # --------------------------------------------------

    def create(self, excel_path):

        print(f"Creating cache : {Path(excel_path).name}")

        df = pd.read_excel(excel_path)

        cache = self.cache_path(excel_path)

        df.to_parquet(cache, index=False)

        self.save_metadata(excel_path, df)

        return cache

    # --------------------------------------------------

    def load(self, excel_path):

        cache = self.cache_path(excel_path)

        print(f"Loading cache : {cache.name}")

        return pd.read_parquet(cache)

    # --------------------------------------------------

    def load_or_create(self, excel_path):

        if self.is_cache_valid(excel_path):

            return self.load(excel_path)

        self.create(excel_path)

        return self.load(excel_path)
    
    #---------------------------------------------------------
    def save_metadata(self, excel_path, df):

        excel_path = Path(excel_path)

        metadata = {

            "dataset_name": excel_path.stem,

            "original_file": str(excel_path),

            "rows": len(df),

            "columns": len(df.columns),

            "column_names": list(df.columns),

            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "ecat_version": "1.3.1"

        }

        json_path = self.dataset_folder / (
            excel_path.stem + ".json"
        )

        with open(json_path, "w", encoding="utf-8") as f:

            json.dump(metadata, f, indent=4)
            
    #---------------------------------------------------------------------
    def available_datasets(self):

        datasets = []

        for file in sorted(self.dataset_folder.glob("*.json")):

            with open(file, encoding="utf-8") as f:

                datasets.append(json.load(f))

        return datasets
        
    # --------------------------------------------------

    def load_dataset(self, dataset_name):

        cache = self.dataset_folder / f"{dataset_name}.parquet"

        return pd.read_parquet(cache)
        
    # --------------------------------------------------

    def delete_dataset(self, dataset_name):

        parquet = self.dataset_folder / f"{dataset_name}.parquet"

        json_file = self.dataset_folder / f"{dataset_name}.json"

        if parquet.exists():

            parquet.unlink()

        if json_file.exists():

            json_file.unlink()
            
    # --------------------------------------------------

    def refresh_dataset(self, excel_path):

        self.create(excel_path)