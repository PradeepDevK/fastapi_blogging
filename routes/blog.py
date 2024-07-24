from fastapi import APIRouter
from models.blog import BlogModel, UpdateBlogModel
from config.config import blogs_collection
from serializers.blog import DecodeBlog, DecodeBlogs
import datetime
from bson import ObjectId

blog_route = APIRouter()

# post request
@blog_route.post("/new/blog")
def NewBlog(doc: BlogModel):
    doc = dict(doc)
    current_datetime = datetime.date.today()
    doc["createdDate"] = str(current_datetime)
    
    resposne = blogs_collection.insert_one(doc)
    
    doc_id = str(resposne.inserted_id)
    return {
        "status": "OK",
        "message": "Blog posted successfully.",
        "_id": doc_id
    }
    
# getting blogs
@blog_route.get("/all/blogs")
def AllBlogs():
    response = blogs_collection.find()
    decoded_data = DecodeBlogs(response)
    
    return {
        "status": "OK",
        "data": decoded_data
    }
    
# get blog by _id
@blog_route.get("/blog/{_id}")
def getBlogById(_id:str):
    response = blogs_collection.find_one({ "_id": ObjectId(_id)})
    decoded_data = DecodeBlog(response)
    
    return {
        "status": "OK",
        "data": decoded_data
    }
    
# update blog
@blog_route.patch("/update/{_id}")
def updateBlog(_id:str, doc: UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True))
    
    blogs_collection.find_one_and_update({ "_id": ObjectId(_id) }, {
        "$set": req
    });
        
    return {
        "status": "OK",
        "message": "Blog updated successfully."
    }
    
@blog_route.delete("/delete/{_id}")
def deleteBlog(_id: str):
    blogs_collection.delete_one({ "_id": ObjectId(_id)})
    
    return {
        "status": "OK",
        "message": "Blog deleted successfully."
    }