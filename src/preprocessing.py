import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    df = df.dropna()
    return df


def prepare_features(df):
    features = df[["Age", "AnnualIncome", "SpendingScore"]]
    return features