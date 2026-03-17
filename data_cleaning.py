import pandas as pd

def clean_data():

    df = pd.read_csv("../data/raw_data.csv")

    print("Original shape:", df.shape)

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna(subset=['city','cuisine','rating','cost'])

    # Convert rating
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df = df[(df['rating'] > 0) & (df['rating'] <= 5)]

    # Clean cost
    df['cost'] = df['cost'].astype(str).str.replace('[^0-9]', '', regex=True)
    df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
    df = df[df['cost'] > 0]

    # Clean rating_count (remove text like "20+ ratings")
    df['rating_count'] = df['rating_count'].astype(str).str.replace('[^0-9]', '', regex=True)
    df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce').fillna(0)

    print("Cleaned shape:", df.shape)

    df.to_csv("../data/cleaned_data.csv", index=False)

if __name__ == "__main__":
    clean_data()