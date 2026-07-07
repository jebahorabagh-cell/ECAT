from pathlib import Path

from app.services.dataset_cache import DatasetCache


class DatasetManager:

    def __init__(self):

        self.cache = DatasetCache()

    # --------------------------------------------------

    def import_dataset(self, excel_file):

        self.cache.load_or_create(excel_file)

    # --------------------------------------------------

    def datasets(self):

        return self.cache.available_datasets()

    # --------------------------------------------------

    def dataset_names(self):

        return [

            d["dataset_name"]

            for d in self.datasets()

        ]

    # --------------------------------------------------

    def exists(self, dataset_name):

        return dataset_name in self.dataset_names()