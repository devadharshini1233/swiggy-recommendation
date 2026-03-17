import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

def preprocess():

    df = pd.read_csv("../data/cleaned_data.csv")

    print("Data loaded:", df.shape)

    # Reduce rare cuisines (important optimization)
    top_cuisines = df['cuisine'].value_counts().head(20).index
    df['cuisine'] = df['cuisine'].apply(
        lambda x: x if x in top_cuisines else "Other"
    )

    categorical_cols = ['city', 'cuisine']
    numerical_cols = ['rating', 'rating_count', 'cost']

    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

    encoded = encoder.fit_transform(df[categorical_cols])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out()
    )

    final_df = pd.concat(
        [df[numerical_cols].reset_index(drop=True),
         encoded_df.reset_index(drop=True)],
        axis=1
    )

    print("Encoded shape:", final_df.shape)

    # Save encoded data
    final_df.to_csv("../data/encoded_data.csv", index=False)

    # Save encoder
    with open("../models/encoder.pkl", "wb") as f:
        pickle.dump(encoder, f)

    print("Preprocessing completed!")

if __name__ == "__main__":
    preprocess()