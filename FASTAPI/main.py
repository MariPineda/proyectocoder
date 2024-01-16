"""from fastapi import FastAPI
from pydantic import BaseModel

from typing import Union


class Item(BaseModel):
    nombre: str
    precio: float
    descripcion: Union[str, None] = None


#levantamos una instancia de la clase FASTAPI

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {"detail": "Hola mundo!!!"}

@app.get("/items/{id}")
def leer_items(id: int, cantidad: Union[int, None] = None):
    return {"detail": f"Se envió el: {id}, cantidad: {cantidad}"}

@app.post("/items/")
def crear_item(item: Item):
    print(item)
    return {"detail": "Se creo el item"}


c:
R:
U:
D:
"""

"""
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

#Modelo
class Articulo(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None
    precio: float
    impuesto: float | None = None

app = FastAPI() 

#Simulación DB
lista_articulos = []

#Endpoints
@app.post("/articulos")
def crear_articulo(articulo: Articulo):
    articulo_dict = articulo.to_dict()
    lista_articulos.append(articulo_dict)

    return articulo

@app.get("/articulos")
def leer_articulos():
    print(lista_articulos)
    return lista_articulos

@app.get("/articulos/{articulo_id}")
def leer_articulo(articulo_id: int):

    for i in range(len(lista_articulos)):
        if articulo_id == lista_articulos[i].get("id"):
            return JSONResponse(status_code=status.HTTP_200_OK, content=lista_articulos[i])

    return JSONResponse (status_code=status.HTTP_404_NOT_FOUND, content=f"No se encontro el articulo {articulo_id}")
                        

@app.put("/articulos/{articulo_id}")
def update_articulo(articulo_id: int, mod_articulo: Articulo):
    
@app.delete("/articulos/{articulo_id}")
def eliminar_articulo(articulo_id: int):
    for i in range(len(lista_articulos)):
        if articulo_id == lista_articulos[i].get("id"):
            lista_articulos.pop(i)
            return JSONResponse(status_code=status.HTTP_"==_OK, content=f"Se elimino el id: {articulo_id})
    raise HTTPException(status_code=status.)
"""