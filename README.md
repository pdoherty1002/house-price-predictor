# House Price Predictor

A full-stack application predicting house prices, built to demonstrate integration across a Python ML service and a .NET application — a distinct project from pure ML/data science work, focused on real cross-language architecture.

## Architecture

```
Blazor front-end  →  ASP.NET Core API  →  FastAPI (Python)  →  scikit-learn model
```

- **Blazor front-end** (`blazor-app`) — form for entering house details, displays the predicted price
- **ASP.NET Core API** (`dotnet-api`) — receives requests from the front-end, calls the Python service, handles connection failures gracefully
- **FastAPI service** (`python-service`) — loads the trained model, validates and encodes incoming data to match the model's expected input, returns a prediction
- **Shared** — a small shared class library so the `HouseFeatures` data shape has one single definition used by both `dotnet-api` and `blazor-app`, rather than being duplicated

See [python-service/README.md](python-service/README.md) for details on the model itself, its features, and results.

## Running locally

Three services need to be running at the same time, each in its own terminal:

```
# Python service
cd python-service
venv\Scripts\activate
uvicorn main:app --reload

# .NET API
cd dotnet-api
dotnet run

# Blazor front-end
cd blazor-app
dotnet run
```

Then open the Blazor app's URL in a browser — the prediction form is the homepage.

## Dependencies

- **Python** (`python-service`): see `requirements.txt` — install with `pip install -r requirements.txt`
- **.NET** (`dotnet-api`, `blazor-app`): dependencies are managed via each project's `.csproj` file (`<PackageReference>` entries) — no separate requirements file needed. Running `dotnet run` or `dotnet build` restores them automatically.

## Status

Working end-to-end — a real prediction flows through all three layers and displays on the page.

The front-end is a single-page app. Of the model's 10 features, 6 are user-adjustable (lot size, overall quality, overall condition, year built, bedrooms, kitchen quality) via dropdowns and a date picker, while the remaining 4 (dwelling type, zoning, neighborhood, lot shape) are fixed to sensible, typical defaults — keeping the demo quick and approachable rather than requiring 10 fields to be filled in manually.
