# import packages
import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path):
    """
    Cleans the data by dropping all missing entries (listwise deletion)
    """
    current_directory = os.getcwd()
    df = pd.read_csv(f"{input_path}diabetes.csv")
    col_check = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for i in col_check:
        df[i] = df[i].replace(to_replace = 0, value = np.NaN)
    df.dropna(inplace= True)
    df.to_csv(f"{output_path}data_clean.csv", index=False)

if __name__ == "__main__":
    clean_data(input_path = "data/raw/", output_path = "data/clean/")