# main.py
import os
import pandas as pd
from data_loader import CSVLoader
from analyzer import LeastSquaresSelector
from mapper import Mapper
from database import DBManager
from visualizer import plot_mappings

def main():
    # Use single training CSV
    training_path = 'data/train.csv'
    ideal_path = 'data/ideal.csv'
    test_path = 'data/test.csv'

    # Load datasets
    training_df = CSVLoader(training_path).load()
    ideal_df = CSVLoader(ideal_path).load()
    test_df = CSVLoader(test_path).load()

    # Database
    db = DBManager()
    db.save_dataframe(training_df, 'training')
    db.save_dataframe(ideal_df, 'ideal_functions')

    # Least squares selection
    selector = LeastSquaresSelector()
    selected, max_devs = selector.select_ideal_functions(training_df, ideal_df)

    # Map test data
    mapper = Mapper(selected, ideal_df, max_devs)
    mapping_df = mapper.map_dataset(test_df)
    db.save_dataframe(mapping_df, 'mapping')

    # Visualization
    os.makedirs('output', exist_ok=True)
    plot_mappings(training_df, ideal_df, selected, mapping_df, max_devs, output_path='output/result.html')

if __name__ == '__main__':
    main()
