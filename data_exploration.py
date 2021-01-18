import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def count_missing_data(df):
    """ Iterates each column and counts number of missing values
    Args:
        df (pandas.DataFrame): dataframe

    Returns:
        dict: missing data counts (value) for each column (key)
    """
    output_data = {}
    for column in df.columns:
        output_data[column] = df[column].isna().sum()

    return output_data


def main():
    data_dir = "./widsdatathon2021/"
    training_data_path = data_dir + "TrainingWiDS2021.csv"
    data_info_dict = data_dir + "DataDictionaryWiDS2021.csv"

    train_df = pd.read_csv(training_data_path, index_col=0)

if __name__ == "__main__":
    main()