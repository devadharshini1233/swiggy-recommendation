from recommender import Recommender

model = Recommender()

# 👇 ADD THIS LINE HERE
print(model.clean_df['name'].head(10))

# Test recommendation
result = model.recommend("Paradise Biryani")

print(result)
