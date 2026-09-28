from fastapi import FastAPI
app = FastAPI()

@app.get("/users/me")
async def get_auther_name():
    return {"author name" : 67}