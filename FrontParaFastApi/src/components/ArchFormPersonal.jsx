import React from "react";
import axiosInstance from "../api/axioInstance";


const CargarPersonalBtn = async (e) => {
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
    Descripccion,

  }
  console.log(nuevoRegistro);
  try {
    const response = await axiosInstance.post("http://127.0.0.1:8000/personalPost", nuevoRegistro);
    console.log("el nuevo registro fue un exito...", nuevoRegistro);
    
  } catch (error) {
    if (error.response) {
      console.error("Error del servidor:", error.response.data);
    } else {
      console.error("Error de la solicitud:", error.message);
    }

  }