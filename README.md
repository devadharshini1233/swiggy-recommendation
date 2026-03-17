# swiggy-recommendation
A content-based restaurant recommendation system built using Python and Scikit-learn, with an interactive Streamlit web app that provides personalized suggestions based on user preferences like cuisine, cost, rating, and location.





# 🍽️ Swiggy Restaurant Recommendation System

An intelligent restaurant recommendation system built using Machine Learning and deployed with Streamlit. The application suggests similar restaurants based on user preferences such as cuisine, cost, rating, and location.

---

## 🚀 Features

- 🔍 Search and select restaurants
- 📍 Filter by city
- ⭐ Filter by rating
- 💰 Filter by cost
- 🍜 Filter by cuisine
- 🤖 Content-based recommendation using cosine similarity
- 🎨 Interactive and user-friendly Streamlit UI

---

## 🧠 How It Works

The system uses a content-based filtering approach:

- Data is preprocessed and cleaned
- Categorical features (city, cuisine) are encoded using OneHotEncoder
- Numerical features (rating, cost, rating count) are combined with encoded features
- Cosine similarity is used to compute similarity between restaurants
- Top similar restaurants are recommended to the user
- 
---

▶️ Run the Application
streamlit run app.py
🌐 Deployment

The project can be deployed using Streamlit Cloud for easy access and sharing.
🧰 Tech Stack

Python
Pandas
Scikit-learn
Streamlit

## ⚙️ Installation

`bash
git clone https://github.com/your-username/swiggy-recommendation.git
cd swiggy-recommendation
pip install -r requirements.txt


📌 Future Improvements
Add restaurant images
Improve recommendation accuracy
Add user-based recommendations
Integrate database support
Deploy with scalable backend

👩‍💻 Author
Devadharshini
⭐ Support
If you like this project, consider giving it a ⭐ on GitHub!

