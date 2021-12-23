from fastapi import FastAPI
from magnum import Mangum
from api.v1.api import router as api_router
app = FastAPI()

app.include_router(api_router,prefix="/api/v1")

@app.get("/",tags=["sample root "])
async def sample():
    return {"hello": "world"}

handler = Mangum(app)