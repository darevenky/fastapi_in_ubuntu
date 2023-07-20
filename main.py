from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app=FastAPI()


@app.get('/')
def index():
    return {'hello':'it is working'}


@app.get('/about')
def about():
    return {'data':'about page'}




#getting all the blogs

@app.get('/blogs')
def index():
    return {'data':'blog list'}


@app.get('/blog')
def index(limit=10,published:bool=True, sort : Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}



@app.get('/blog/unpublished_blogs')
def unpublished_blogs():
    return {'data':'all unpublished_blogs'}




#getting the blob with id(path parameters)

@app.get('/blog/{blog_id}')
def index(blog_id:int):                 
    return {'data':{'blog':blog_id}}




#getting comments from blog id

@app.get('/blog/{blog_id}/comments')
def index(blog_id:int):
    return {blog_id:'comments'}


class Blog(BaseModel):
    name:str
    body:str
    published:bool | None=None



@app.post('/')
def new_blog(blog:Blog):
    return {'success':f'blog is created with {blog.name} name'}