# House Price Predictor — Python Service

A linear regression model used to predict house prices based on a subset of features from the Kaggle "House Prices — Advanced Regression Techniques" dataset (`train.csv`).

## Features

A subset of 10 features was deliberately selected from the dataset's full 79 columns, rather than pursuing exhaustive feature engineering. This project's primary goal is demonstrating a broader range of skills — specifically, a full-stack architecture connecting a Python ML service to a .NET application — so the modeling work here is intentionally kept focused rather than exhaustive.

**Features used**: `MSSubClass`, `MSZoning`, `LotArea`, `LotShape`, `Neighborhood`, `OverallQual`, `OverallCond`, `YearBuilt`, `BedroomAbvGr`, `KitchenQual`

## Results

The baseline model achieved an R² of 0.78 and a Mean Absolute Error of £27,358.65 (roughly 15% of the average house price) — a reasonable, "fair" result given the deliberately limited feature set and effort invested, consistent with this project's focus on architecture over exhaustive modeling.

Two feature engineering experiments were tried in an attempt to improve on this baseline:
- **Grouping rare neighborhood categories** (fewer than 15 examples) into a single "Rare" category — no meaningful change (MAE £27,537.34, R² 0.78)
- **Engineering a `HouseAge` feature** (sale year minus build year) — no meaningful change (MAE £27,358.95, R² 0.78)

Neither experiment meaningfully improved results, suggesting the model's performance is already largely driven by its strongest existing features (e.g. `OverallQual`). Future versions could explore additional features, more advanced models (e.g. Random Forest, XGBoost), or more thorough feature engineering to improve accuracy further.
