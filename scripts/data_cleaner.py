import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
    
    def load_data(self):
        """Load the data from a CSV file."""
        return pd.read_csv(self.file_path)
    
    def handle_missing_values(self):
        """Handle missing values in categorical columns."""
        missing_counts = self.data.isnull().sum()
        total_rows = len(self.data)
        for col in self.data.columns:
            if self.data[col].dtype == 'object':  # Check if column is categorical
                missing_percentage = (missing_counts[col] / total_rows) * 100
                if missing_percentage > 50:
                    self.data.drop(columns=[col], inplace=True)
                elif missing_percentage > 0:
                    self.data[col].fillna(method='bfill', inplace=True)  # Fill missing values with next valid value
        return self.data
    
    def handle_outliers(self, columns, method='clip'):
        """Handle outliers using specified method (clip, remove)."""
        if method == 'clip':
            for col in columns:
                self.data[col] = self.data[col].clip(lower=self.data[col].quantile(0.05), upper=self.data[col].quantile(0.95))
        elif method == 'remove':
            for col in columns:
                q1 = self.data[col].quantile(0.25)
                q3 = self.data[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                self.data = self.data[(self.data[col] >= lower_bound) & (self.data[col] <= upper_bound)]
        else:
            raise ValueError("Invalid outlier handling method. Choose from 'clip' or 'remove'.")
    
    def preprocess_data(self, outlier_method='clip', outlier_columns=None):
        """Preprocess the data."""
        # Handle missing values
        self.handle_missing_values()
        
        # Handle outliers
        if outlier_columns:
            self.handle_outliers(columns=outlier_columns, method=outlier_method)
        
        return self.data
