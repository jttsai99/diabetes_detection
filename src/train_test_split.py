import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_path, output_path, test_size = 0.2):
    """
    Read data and conduct train/test split; save resulting sets as csv. output_path (ie. "data/processed")
    is the directory containing the splitted train test csv.
    """
    df = pd.read_csv(f"{input_path}data_clean.csv")
    df_train, df_test = train_test_split(df, test_size=test_size, shuffle=True, random_state=0)

    # Save
    df_train.to_csv(f"{output_path}data_train.csv", index=False)
    df_test.to_csv(f"{output_path}data_test.csv", index=False)
    return 

if __name__ == "__main__":
    split_data(input_path = "data/clean/", output_path = "data/processed/")