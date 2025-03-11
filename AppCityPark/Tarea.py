from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import CleverCursor

createTareaRouter = APIRouter()

class Tarea(BaseModel):
    id_Tarea: int
    id_cliente: int
    Descripcion: str
    Tipo : str
    fecha_solicitud: str
    fecha_finalizacion: str
    estado: str
    personal_Mantenimiento: str
    
@createTareaRouter.post("/tarea")
async def create_tarea(tarea: Tarea):
    query = f"INSERT INTO Tarea (id_Tarea, id_cliente, Descripcion, Tipo, fecha_solicitud, fecha_finalizacion, estado, personal_Mantenimiento) VALUES ({tarea.id_Tarea}, {tarea.id_cliente}, '{tarea.Descripcion}', '{tarea.Tipo}', '{tarea.fecha_solicitud}', '{tarea.fecha_finalizacion}', '{tarea.estado}', '{tarea.personal_Mantenimiento}')"
    CleverCursor.execute(query)
    CleverCursor.commit()
    return {"message": "Tarea created successfully"}