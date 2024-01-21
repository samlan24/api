from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "My first API"}

@app.get("/post")
def get_post():
    return {"data": "this is your post"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"mess": "created post"}