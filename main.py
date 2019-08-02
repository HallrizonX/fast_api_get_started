from fastapi import FastAPI
from notes.views import notes_router

app = FastAPI()

app.include_router(notes_router)
