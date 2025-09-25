from fastapi import APIRouter, HTTPException, Query
from bson import ObjectId
from bson.errors import InvalidId
from db import db
from models import Post
from datetime import datetime

router = APIRouter()
collection = db["posts"]

def post_helper(post):
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
        "author": post["author"],
        "created_at": post.get("created_at")
    }

@router.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["created_at"] = datetime.now().isoformat()
    result = await collection.insert_one(post_dict)
    new_post = await collection.find_one({"_id": result.inserted_id})
    return {"message": "Post created", "post": post_helper(new_post)}

@router.get("/posts")
async def list_posts(author: str = Query(None)):
    query = {"author": author} if author else {}
    posts = []
    async for post in collection.find(query):
        posts.append(post_helper(post))
    return posts

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    try:
        obj_id = ObjectId(post_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")
    deleted = await collection.delete_one({"_id": obj_id})
    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
