from typing import Union
from fastapi import FastAPI
from usuario_map import usuarioRouter
from cargo_map import cargoRouter
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from Tarea import TareaRouter
from cliente import ClienteRouter 
=======
from Tarea import TareaRouter  
>>>>>>> 87480d9410d3fe8e1c296b3e32129ed2ac0ed65e

app = FastAPI()
app.include_router(usuarioRouter)
app.include_router(cargoRouter)
<<<<<<< HEAD
app.include_router(ClienteRouter)
=======
>>>>>>> 87480d9410d3fe8e1c296b3e32129ed2ac0ed65e
app.include_router(TareaRouter)



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

#solo parametro la url debe enviarse: "http://127.0.0.1:8000/items/?q=infoComoParametro"
@app.get("/items/")
async def read_param_item(q: Union[str, None] = None):
    return {"q": q}

#solo info como parte de la url debe enviarse: "http://127.0.0.1:8000/items/5"
@app.get("/items/{item_id}")
async def read_paramInPath_item(item_id: int):
    return {"item_id": item_id}

#realizar envio de información de las 2 formas en simultánea en la url debe enviarse: "http://127.0.0.1:8000/items/5?q=infoComoParametro"
@app.get("/items/{item_id}")
async def read_both_paramTypes_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
@app.delete("/items_del/{item_id}")
async def delete_by_id(item_id: int):
    return {"resultado": "Se ha eliminado correctamente el item solicitado"}
    
    
    