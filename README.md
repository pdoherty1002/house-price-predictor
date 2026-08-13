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

Then open the Blazor app's URL in a browser and navigate to `/predict`.

## Status

Working end-to-end — a real prediction flows through all three layers and displays on the page.

This is a **work in progress**. Current known limitations and next steps:
- The form currently requires all 10 feature values to be typed in manually — too much friction for a quick demo. Next step is adding sensible filler/default values and converting the categorical fields (zoning, neighborhood, etc.) into dropdowns instead of free text.
- Visual styling is minimal — functional but not yet polished.
