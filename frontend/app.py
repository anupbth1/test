from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

API = "http://localhost:8000/status"


@app.get("/", response_class=HTMLResponse)
def dashboard():
    try:
        data = requests.get(API).json()
    except:
        data = {}

    html = f"""
    <html>
    <head><title>AI Researcher Dashboard</title></head>
    <body style="font-family:Arial">
        <h1>AI Researcher</h1>
        <p><b>Active:</b> {data.get("active")}</p>
        <p><b>Goal:</b> {data.get("goal")}</p>
        <p><b>Last Update:</b> {data.get("last_update")}</p>
        <p><b>Last Result:</b> {data.get("last_result")}</p>
    </body>
    </html>
    """
    return html
