import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.recommender import Recommender

# Load model
model = Recommender()
df = model.clean_df

# Page config
st.set_page_config(page_title="Swiggy Recommender", layout="wide")

# ------------------ STYLING ------------------
st.markdown("""
<style>
.stButton>button {
    background-color: #fc8019;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.card {
    border:1px solid #ddd;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    background-color:#1e1e1e;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<h1 style='text-align:center;'>🍽️ Swiggy Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Discover restaurants you will love ❤️</p>", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.header("🔍 Filters")

# City
city = st.sidebar.selectbox(
    "Select City",
    sorted(df['city'].dropna().unique())
)

# Filters
min_rating = st.sidebar.slider("Minimum Rating ⭐", 0.0, 5.0, 3.5, 0.1)
max_cost = st.sidebar.slider("Max Cost 💰", 50, 1000, 500)

cuisine_filter = st.sidebar.selectbox(
    "Cuisine 🍜",
    ["All"] + sorted(df['cuisine'].dropna().unique())
)

# ------------------ FILTER DATA ------------------
filtered_df = df[df['city'] == city]
filtered_df = filtered_df[filtered_df['rating'] >= min_rating]
filtered_df = filtered_df[filtered_df['cost'] <= max_cost]

if cuisine_filter != "All":
    filtered_df = filtered_df[filtered_df['cuisine'] == cuisine_filter]

# Handle no data
if filtered_df.empty:
    st.warning("No restaurants match your filters 😢")
    st.stop()

# ------------------ RESTAURANT SELECT ------------------
restaurant_list = filtered_df['name'].drop_duplicates()

# limit for performance
if len(restaurant_list) > 200:
    restaurant_list = restaurant_list.sample(200)

restaurant = st.selectbox(
    "🔎 Search / Choose Restaurant",
    sorted(restaurant_list)
)

# ------------------ BUTTON ------------------
if st.button("✨ Get Recommendations"):

    results = model.recommend(restaurant)

    if isinstance(results, str):
        st.error(results)
    else:
        st.subheader("🍴 Top Recommendations for You")

        col1, col2 = st.columns(2)

        for i, (_, row) in enumerate(results.iterrows()):

            card = f"""
            <div class="card">
                <h4>🍽️ {row['name']}</h4>
                <p>📍 {row['city']}</p>
                <p>🍜 {row['cuisine']}</p>
                <p>⭐ {row['rating']} | 💰 ₹{row['cost']}</p>
            </div>
            """

            if i % 2 == 0:
                col1.markdown(card, unsafe_allow_html=True)
            else:
                col2.markdown(card, unsafe_allow_html=True)