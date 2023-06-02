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
let numeroParImpar = (numero) => {
if (numero%2==0)
{
    document.getElementById("resultado").innerHTML =
      "<span>El numero " + numero + " es: </span><span class='respuesta'>Par</span>";
}else{
    document.getElementById("resultado").innerHTML =
    "<span>El numero " + numero + " es: </span><span class='respuesta'>Impar</span>";
}

  };
  