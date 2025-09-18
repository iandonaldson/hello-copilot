# Build a minimal FastAPI app with one GET /health endpoint returning {"status": "ok"}.
# Add a second endpoint /sum that accepts two query params (a, b) and returns their sum as JSON.
# Include type hints and docstrings. Keep it simple and production-friendly.




from fastapi import FastAPI, Query
from typing import Dict
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health", response_model=Dict[str, str])
def health() -> Dict[str, str]:
    """
    Health check endpoint.
    Returns status ok.
    """
    return {"status": "ok"}

@app.get("/sum")
def sum_endpoint(a: int = Query(..., description="First integer"), b: int = Query(..., description="Second integer")) -> Dict[str, int]:
    """
    Returns the sum of two integers provided as query parameters.
    """
    return {"sum": a + b}

# To run: uvicorn src.app:app --reload
