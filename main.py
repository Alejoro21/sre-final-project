from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Calculator</h1>
            <form action="/calculate" method="post">
                <input type="number" name="a" step="any" required>
                <input type="number" name="b" step="any" required>

                <select name="operation">
                    <option value="add">+</option>
                    <option value="subtract">-</option>
                    <option value="multiply">*</option>
                    <option value="divide">/</option>
                </select>

                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    """

@app.post("/calculate", response_class=HTMLResponse)
def calculate(a: float = Form(...), b: float = Form(...), operation: str = Form(...)):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b if b != 0 else "Error"
    else:
        result = "Invalid"

    return f"""
    <html>
        <body>
            <h1>Result: {result}</h1>
            <a href="/">Back</a>
        </body>
    </html>
    """
