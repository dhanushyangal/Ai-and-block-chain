import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv('credit_data.csv')

# Features and target
X = data.drop('credit_score', axis=1)
y = data['credit_score']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'credit_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
