# mapper.py
import pandas as pd
import numpy as np
from math import sqrt
from exceptions import MappingException

class Mapper:
    def __init__(self, selected_indices, ideal_df, max_devs):
        self.selected = selected_indices
        self.ideal_df = ideal_df
        self.max_devs = max_devs

    def _ideal_y(self, index, x_val):
        col = f'Y{index}'
        return float(np.interp(x_val, self.ideal_df['X'], self.ideal_df[col]))

    def map_point(self, x, y):
        best_index = None
        best_dev = float('inf')
        for idx in self.selected:
            ideal_y = self._ideal_y(idx, x)
            dev = abs(y - ideal_y)
            if dev <= sqrt(2) * self.max_devs[idx] and dev < best_dev:
                best_index = idx
                best_dev = dev
        if best_index is None:
            raise MappingException(f"Point ({x}, {y}) could not be mapped")
        return best_index, best_dev

    def map_dataset(self, test_df):
        rows = []
        for _, row in test_df.iterrows():
            x, y = row['X'], row['Y']
            try:
                idx, dev = self.map_point(x, y)
            except MappingException:
                idx, dev = None, None
            rows.append({'X': x, 'Y': y, 'IdealFunc': idx, 'DeltaY': dev})
        return pd.DataFrame(rows)
