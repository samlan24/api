from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "My first API"}

@app.get("/post")
def get_post():
    return {"data": "this is your post"}