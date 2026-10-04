from fastapi import FastAPI
from .routers import users
app = FastAPI()


app.include_router(
        users.router,
        prefix="/lund",
        tags=["Users"]
)
@app.get("/users/me")
async def get_auther_name():
    return {"author name" : 67}