from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional,Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn

app = FastAPI()

posts = []

class Post(BaseModel):
    id: Optional[str]
    titulo: str
    autor: str
    contenido: Text
    creado: datetime = datetime.now()
    fpublicacion: Optional[datetime]
    publicado: Optional[bool] = False

@app.get('/')
def index():
    return {"bienvenido": "Hola que tal"}

@app.get('/ver-posts')
def ver_posts():
    return posts


@app.post('/agregar-post')
def agregar_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/ver-post/{post.id}')
def ver_post_id(post_id:str):
    for post in posts:
        if post['id'] == post_id:
            return post
    return HTTPException(status_code=400, detail="No se encontró el post")

@app.put('/actualizar-post/{post.id}')
def actualizar_post(post_id:str, updatePost:Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['titulo'] = updatePost.dict()['titulo']
            posts[index]['autor'] = updatePost.dict()['autor']
            posts[index]['contenido'] = updatePost.dict()['contenido']
            return {"message": "Se actualizó correctamente"}
        
    return HTTPException(status_code=400, detail="No se encontró el post")

@app.delete('/eliminar-post/{post.id}')
def eliminar_post(post_id:str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            #Eliminarlo
            posts.pop(index)
            return {"message": "Se eliminó correctamente"}
    return HTTPException(status_code=400, detail="No se encontró el post")