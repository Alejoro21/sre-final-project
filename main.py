from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import Counter, generate_latest

app = FastAPI(title="SRE Calculator API")

templates = Jinja2Templates(directory="templates")

# Prometheus Metrics
calc_requests_total = Counter(
    "calc_requests_total",
    "Total calculator requests by operation",
    ["operation"]
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None
    })

@app.post("/calculate", response_class=HTMLResponse)
def calculate(
    request: Request,
    a: float = Form(...),
    b: float = Form(...),
    operation: str = Form(...)
):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    calc_requests_total.labels(operation=operation).inc()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "a": a,
        "b": b,
        "operation": operation
    })

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
