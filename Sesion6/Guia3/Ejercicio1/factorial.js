//Funcion para validar solo enteros
let soloNumeros = (numero) => {
  let key = window.Event ? numero.which : numero.keyCode;
  return (key >= 48 && key <= 57) || key == 8;
};

//Funcion para validar números mayor a 0
let pierdeFoco = (numero) => {
  let valor = numero.value.replace(/^0*/, "");
  numero.value = valor;
};

//Funcion para habilitar boton
let enableButton = (numero) => {
  let txtNumero = document.getElementById("numero").value;
  if (txtNumero > 0) {
    document.getElementById("btnFactorial").disabled = false;
  } else {
    document.getElementById("btnFactorial").disabled = true;
  }
};

//Función para calcular factorial de un número
let factorial = (numero) => {
  let inicio = 1;

  for (i = 1; i <= numero; i++) {
    inicio = inicio * i;
  }
  document.getElementById("resultado").innerHTML =
    "<span>El factorial de " +
    numero +
    ' es: </span><span class="respuesta">' +
    inicio +
    "</span>";
  //   alert("El factorial de " + numero + " es: " + inicio);
};
