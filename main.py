from argparse import OPTIONAL
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: OPTIONAL[int] = None
    # TypeError: string indices must be integers
    rating: int = None    


@app.get("/")
def root():
    return {"message": "Reload check 222"}

@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}

@app.post("/createposts")
def create_posts(post:Post):
    print(post.dict())
    return{"data": post}
# Title: str, content: str,
