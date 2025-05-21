from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn
import datetime
 

TareaRouter = APIRouter()

class Tarea(BaseModel):
    id_tarea: str
    id_cliente: str
    descripcion: str
    tipo : str
    fecha_solicitud: datetime.date
    fecha_finalizacion: datetime.date
    estado: str
    personal_mantenimiento: str
    
@TareaRouter.post("/tareaPost")
async def create_tarea(tarea: Tarea):
    query = f"INSERT INTO Tarea (id_Tarea, id_cliente, Descripcion, Tipo, fecha_solicitud, fecha_finalizacion, estado, personal_Mantenimiento) VALUES ({tarea.id_tarea}, {tarea.id_cliente}, '{tarea.descripcion}', '{tarea.tipo}', '{tarea.fecha_solicitud}', '{tarea.fecha_finalizacion}', '{tarea.estado}', '{tarea.personal_mantenimiento}')"
    cleverCursor.execute(query)
    mysqlConn.commit()
    return {"message": "Tarea created successfully"}

