from fastapi import FastAPI
from src.modules.member_entry.routes import router as member_entry_route

app = FastAPI()

app.include_router(member_entry_route)

@app.get("/")
async def root():
    return {"message": "Hello World"}