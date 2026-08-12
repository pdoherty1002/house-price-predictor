import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import os
import joblib

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "house-prices-advanced-regression-techniques", "train.csv")
df = pd.read_csv(csv_path)

# trim to use selected columns
selected_columns = ["MSSubClass", "MSZoning", "LotArea", "LotShape", "Neighborhood", "OverallQual", "OverallCond", "YearBuilt", "BedroomAbvGr", "KitchenQual", "SalePrice"]
trimmed_df = df[selected_columns]

df_encoded = pd.get_dummies(trimmed_df, columns=["MSZoning", "LotShape", "Neighborhood", "KitchenQual"])

# Features and target
X = df_encoded.drop("SalePrice", axis=1)
y = df_encoded["SalePrice"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: £{mae:.2f}")
print(f"R² Score: {r2:.2f}")

joblib.dump(model, "house_price_model.pkl")
joblib.dump(X_train.columns.tolist(), "model_columns.pkl")