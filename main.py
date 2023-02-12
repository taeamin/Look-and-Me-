from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from motor.motor_asyncio import AsyncIOMotorClient

from odmantic import AIOEngine
from config import MONGO_DB_NAME, MONGO_URL


Base_DIR = Path(__file__).resolve().parent
app = FastAPI()


templates = Jinja2Templates(directory=Base_DIR/"templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "룩엣미"})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse("index.html", {"request": request, "title": "룩엣미", "keyword": q})


@app.on_event("startup")
async def on_app_start():
    print("hello server")
    client = AsyncIOMotorClient(MONGO_URL)
    engine = AIOEngine(motor_client, database=MONGO_DB_NAME)


@app.on_event("shutdown")
async def on_app_shutdown():
    print("bye server")
