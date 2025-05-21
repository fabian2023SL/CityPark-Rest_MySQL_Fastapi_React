import React from 'react';
import axiosInstance from '../api/axioInstance';


const CargarTareaBtn = async (e) => {
    e.preventDefault();
    const id_tarea = document.querySelector("#id_tarea").value;
    const id_cliente = document.querySelector("#id_cliente").value;
    const descripcion = document.querySelector("#descripcion").value;
    const tipo = document.querySelector("#tipo").value;
    const fecha_solicitud = document.querySelector("#fecha_solicitud").value;
    const fecha_finalizacion = document.querySelector("#fecha_finalizacion").value;
    const estado = document.querySelector("#estado").value;
    const personal_mantenimiento = document.querySelector("#personal_mantenimiento").value;
    

    const nuevoRegistro = {
      id_tarea,
      id_cliente,
      descripcion,
      tipo,
      fecha_solicitud,
      fecha_finalizacion,
      estado,
      personal_mantenimiento

    }
    console.log(nuevoRegistro)
    try {
      const response =  await axiosInstance.post("http://127.0.0.1:8000/tareaPost", nuevoRegistro);
      console.log("el nuevo registro fue un exito..." , nuevoRegistro)
      
    } catch (error) {
      if (error.response) {
        console.error("Error del servidor:", error.response.data);
      } else {
        console.error("Error de la solicitud:", error.message);
      }

    }
  } 

const FormTarea = () => {
  return (
    <>
    <div className='container'>

      <div className="containerForm">
        <h2>Formulario Tarea</h2>
        <form>
            <fieldset>
              <label htmlFor="id_tarea">id_tarea</label>
              <input type="text" id='id_tarea' required />  
            </fieldset>          
            <fieldset>
              <label htmlFor="id_cliente">id_cliente</label>
              <input type="text" id='id_cliente' required />
            </fieldset>
            <fieldset>
              <label htmlFor="descripcion">descripcion</label>
              <input type="text" id='descripcion' required />
            </fieldset>
            <fieldset>
              <label htmlFor="tipo">tipo</label>
              <input type="text" id='tipo' required />
            </fieldset>
            <fieldset>
              <label htmlFor="fecha_solicitud">fecha_solicitud</label>
              <input type="text" id='fecha_solicitud' required />
            </fieldset>
            <fieldset>
              <label htmlFor="fecha_finalizacion">fecha_finalizacion</label>
              <input type="text" id='fecha_finalizacion' required />
            </fieldset>
            <fieldset>
              <label htmlFor="estado">estado</label>
              <input type="text" id='estado' required />
            </fieldset>
            <fieldset>
              <label htmlFor="personal_mantenimiento">personal_mantenimiento</label>
              <input type="text" id='personal_mantenimiento' required />
            </fieldset>
        
            <button type='submit' onClick={CargarTareaBtn}>Cargar Tarea</button>
        </form>
      </div>
    </div>
    </>
  )
}

export default FormTarea;