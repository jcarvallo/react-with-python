from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from app import App

app = FastAPI()
configure(app, App)
