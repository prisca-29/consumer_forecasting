import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
data = pd.read_csv('consumer_data.csv')

# Data Preprocessing
# Assuming the dataset has columns like 'age', 'income', 'purchase_history', 'spend_amount'
# You should adjust feature columns based on your actual dataset
features = ['age', 'income', 'purchase_history']
target = 'spend_amount'

X = data[features]
y = data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the trained model
joblib.dump(model, 'consumer_forecasting_model.pkl')
print("Model saved as 'consumer_forecasting_model.pkl'")

