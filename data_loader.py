# data_loader.py
from abc import ABC, abstractmethod
import pandas as pd
from exceptions import DataLoadException
import re

class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass

class CSVLoader(BaseLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.file_path)
        except Exception as e:
            raise DataLoadException(f"Failed to load CSV: {self.file_path}") from e

        # Normalize headers: 'x' -> 'X'; 'y' -> 'Y'; 'y1'..'yN' -> 'Y1'..'YN'
        mapping = {}
        for col in df.columns:
            if col.lower() == 'x':
                mapping[col] = 'X'
            elif col.lower() == 'y':
                mapping[col] = 'Y'
            else:
                m = re.match(r'^[yY](\d+)$', col)
                if m:
                    mapping[col] = 'Y' + m.group(1)
        if mapping:
            df = df.rename(columns=mapping)
        if 'X' not in df.columns:
            raise DataLoadException("Missing required column 'X'")

        df = df.apply(pd.to_numeric, errors='coerce')
        if df.isna().any().any():
            raise DataLoadException("CSV contains non-numeric or NaN values")

        df = df.groupby('X', as_index=False).mean()
        df = df.sort_values('X').reset_index(drop=True)
        return df
