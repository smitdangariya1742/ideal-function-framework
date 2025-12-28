# database.py
from sqlalchemy import create_engine 
import pandas as pd
from exceptions import DatabaseException

class DBManager:
    def __init__(self, db_path='data/analysis.db'):
        self.engine = create_engine(f'sqlite:///{db_path}')

    def save_dataframe(self, df: pd.DataFrame, table_name: str):
        try:
            df.to_sql(table_name, self.engine, index=False, if_exists='replace')
        except Exception as e:
            raise DatabaseException(f"Failed to save table {table_name}") from e

    def load_dataframe(self, table_name: str) -> pd.DataFrame:
        try:
            return pd.read_sql_table(table_name, self.engine)
        except Exception as e:
            raise DatabaseException(f"Failed to load table {table_name}") from e
