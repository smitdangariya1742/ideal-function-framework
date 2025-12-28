# analyzer.py
import numpy as np

class LeastSquaresSelector:
    """Select ideal functions using least squares"""
    def select_ideal_functions(self, training_df, ideal_df):
        selected_functions = []
        max_deviations = {}

        x_train = training_df['X'].values
        ideal_columns = [c for c in ideal_df.columns if c != 'X']
        ideal_matrix = np.array([
            np.interp(x_train, ideal_df['X'], ideal_df[col]) for col in ideal_columns
        ])

        for idx, col in enumerate(training_df.columns[1:]):
            train_values = training_df[col].values
            errors = np.sum((ideal_matrix - train_values) ** 2, axis=1)
            best_index = int(np.argmin(errors))
            selected_functions.append(best_index + 1)
            max_dev = np.max(np.abs(train_values - ideal_matrix[best_index]))
            max_deviations[best_index + 1] = max_dev

        return selected_functions, max_deviations
