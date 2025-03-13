import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

# Load dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Features and target
X = df[['MedInc', 'HouseAge', 'AveRooms', 'AveOccup']]  # Selecting important features
y = data.target * 100000  # Scaling house prices

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "house_price_model.pkl")
print("✅ Model trained and saved successfully!")
