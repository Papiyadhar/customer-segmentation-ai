from preprocessing import load_data, clean_data, prepare_features
from segmentation import create_segments


df = load_data("src/customer.csv")

df = clean_data(df)

features = prepare_features(df)

labels = create_segments(features)

df["Segment"] = labels

print(df)