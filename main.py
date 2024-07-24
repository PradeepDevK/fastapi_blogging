from fastapi import FastAPI
from routes.entry import router
from routes.blog import blog_route

app = FastAPI()

app.include_router(router)
app.include_router(blog_route)