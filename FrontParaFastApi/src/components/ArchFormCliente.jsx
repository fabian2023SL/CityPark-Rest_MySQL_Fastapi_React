import React from "react";
import axiosInstance from "../api/axioInstance";


const cargarButton = async (e) => {
  e.preventDefault();
  const nombre = document.querySelector("#nombre").value;
  const apellido = document.querySelector("#apellido").value;
  const direccion = document.querySelector("#direccion").value;
  const telefono = document.querySelector("#telefono").value;
  const cod_personal = document.querySelector("#cod_personal").value;
  const solicitud_mantenimiento = document.querySelector("#solicitud_mantenimiento").value;

  const nuevoRegistro = {
    nombre,
    apellido,
    direccion,
    telefono,
    cod_personal,
    solicitud_mantenimiento,

  }
  console.log(nuevoRegistro);
  try {
    const response = await axiosInstance.post( "http://127.0.0.1:8000/cliente", nuevoRegistro);
    console.log("el nuevo registro fue un exito...", nuevoRegistro)

    } catch (error) {
      if (error.response) {
        console.error("Error del servidor:", error.response.data);
      } else {
        console.error("Error de la solicitud:", error.message);
      }

    }
}

const FromCliente = () => {
  return (
    <>
      <div className="container">
        <div className="containerForm">
          <h2>Formulario cliente</h2>
          <form>
            <fieldset>
              <label htmlFor="nombre">Nombre</label>
              <input type="text" id="nombre" required />
            </fieldset>
            <fieldset>
              <label htmlFor="apellido">Apellido</label>
              <input type="text" id="apellido" required />
            </fieldset>
            <fieldset>
              <label htmlFor="direccion">Direccion</label>
              <input type="text" id="direccion" required />
            </fieldset>
            <fieldset>
              <label htmlFor="telefono">Telefono</label>
              <input type="text" id="telefono" required />
            </fieldset>
            <fieldset>
              <label htmlFor="cod_personal">Cod Personal</label>
              <input type="text" id="cod_personal" required />
            </fieldset>
            <fieldset>
              <label htmlFor="solicitud_mantenimiento">Solicitud Mantenimiento</label>
              <input type="text" id="solicitud_mantenimiento" required />
            </fieldset>

            <button type='submit' onClick={cargarButton}>Cargar</button>

          </form>
        </div>
      </div>
    </>
  )
}

export default FromCliente;

     