from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn


ClienteRouter = APIRouter()

class Cliente(BaseModel):
    Nombre: str
    Apellidos: str
    dirreccion: str
    telefono: str
    cod_personal: str
    solicitud_mantenimiento: str

@ClienteRouter.post("/cliente")
async def create_cliente(cliente: Cliente):
    query = f"INSERT INTO Cliente (Nombre, Apellidos, dirrecion, telefono, cod_personal, solicitud_mantenimiento) VALUES ('{cliente.Nombre}', '{cliente.Apellidos}', '{cliente.dirreccion}', '{cliente.telefono}', '{cliente.cod_personal}', '{cliente.solicitud_mantenimiento}')"
    cleverCursor.execute(query)
    mysqlConn.commit()
    return {"message": "Cliente created successfully"}

    
    
    