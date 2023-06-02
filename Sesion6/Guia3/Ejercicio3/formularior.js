//Funcion para validar formulario
let validarFormulario = () => {
  //Inputs required
  let txtNombre = document.getElementById("nombre");
  let txtCorreo = document.getElementById("correo");
  let txtComentarios = document.getElementById("comentarios");

  //Otros Inputs y labels
  let txtContrasenia = document.getElementById("contrasenia");
  let txtMsjComentario = document.getElementById("msj-comentario");
  let txtMsjPassword = document.getElementById("msj-password");
  let btnEnviar = document.getElementById("btn-enviar");

  //Requided input nombre, correo y comentarios 
  txtNombre.required = true;
  txtCorreo.required = true;
  txtComentarios.required = true;

  //Imprimir resultado al enviar los datos
  document.getElementById('msj-formulario').innerHTML = "Datos enviados";

  clearInputs(txtNombre, txtCorreo, txtComentarios, txtContrasenia, txtMsjComentario, txtMsjPassword, btnEnviar);
};

// Función para validar tamaño de campo comentarios
let limiteComentario = (comentario, cantidad) => {
limite = 50;
ncaracteres = comentario.value.length + cantidad;
  console.log(ncaracteres);
  if (ncaracteres > 0 && ncaracteres < 50)
  {
    document.getElementById("msj-comentario").innerHTML =
    ncaracteres + " Caracteres escritos";
  }
  else if(ncaracteres <= 0)
  {
    document.getElementById("msj-comentario").innerHTML =
    0 + " Caracteres escritos";
  }else if(ncaracteres > 50)
  {
    document.getElementById("msj-comentario").innerHTML =
    50 + " Caracteres escritos";
  }

};

// Función para validar contraseña con al menos una letra mayuscula, minuscula y un digito
let validarPassword = (password) => {
  let validar = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;
  let valido = document.getElementById('msj-password');
  let btnEnviar = document.getElementById('btn-enviar');

      if (validar.test(password.value)) {
        valido.innerText = "Contraseña valida";
        btnEnviar.disabled = false;

      } else {
        valido.innerText = "Contraseña no valida";
        btnEnviar.disabled = true;
      }
}

//Función para limpiar datos
let clearInputs = (nombre, correo, comentarios, contrasenia, msjcomentario, msjpassword, btnenviar) => {
  nombre.value = '';
  correo.value = '';
  comentarios.value = '';
  contrasenia.value = '';
  msjcomentario.innerHTML = '0 Caracteres escritos';
  msjpassword.innerHTML = '';
  btnenviar.disabled = true;
}
