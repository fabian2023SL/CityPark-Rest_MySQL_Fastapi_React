from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from Clever_MySQL_conn import cleverCursor, mysqlConn

cargoRouter =  APIRouter()

class CargoDB(BaseModel):
    nombre_cargo : str
    salario : int
    
@cargoRouter.get("/cityPark_cargo/", status_code=status.HTTP_302_FOUND)
async def get_users():
    selectAll_query = 'Select * from cargo'
    cleverCursor.execute(selectAll_query)
    result = cleverCursor.fetchall()
    return result

@cargoRouter.get("/cityPark_cargo/{cargo_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(cargo_id: int):
    select_query = "SELECT * FROM cargo WHERE id_cargo = %s"
    cleverCursor.execute(select_query, (cargo_id,))
    result = cleverCursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    
@cargoRouter.post("/cityPark_crea_cargo/", status_code=status.HTTP_201_CREATED)
def insert_user(cargoPost: CargoDB):
    insert_query = """
    INSERT INTO cargo (nombre_cargo, salario)
    VALUES (%s, %s)
    """
    values = (cargoPost.nombre_cargo, cargoPost.salario)

    try:
        cleverCursor.execute(insert_query, values)
        mysqlConn.commit()
    except mysqlConn.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}


#import hashlib
# Hash the password using SHA-256
# hashed_password = hashlib.sha256(cargoPost.password.encode()).hexdigest()

