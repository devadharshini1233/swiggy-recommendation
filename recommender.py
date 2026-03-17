import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:

    def __init__(self):
        # Get base path (where this file is located)
        base_path = os.path.dirname(__file__)

        # Create correct file paths
        clean_path = os.path.join(base_path, "../data/cleaned_data.csv")
        encoded_path = os.path.join(base_path, "../data/encoded_data.csv")

        # Load datasets
        self.clean_df = pd.read_csv(clean_path)
        self.encoded_df = pd.read_csv(encoded_path)

    def recommend(self, restaurant_name, top_n=5):

        # Get index of selected restaurant
        idx = self.clean_df[
            self.clean_df['name'] == restaurant_name
        ].index

        if len(idx) == 0:
            return "Restaurant not found"

        idx = idx[0]

        # Get input vector
        input_vector = self.encoded_df.iloc[idx].values.reshape(1, -1)

        # Compute similarity
        similarity = cosine_similarity(input_vector, self.encoded_df).flatten()

        # Get top similar indices
        similar_indices = similarity.argsort()[-top_n-1:-1][::-1]

        # Return results
        return self.clean_df.iloc[similar_indices][
            ['name','city','cuisine','rating','cost']
        ]