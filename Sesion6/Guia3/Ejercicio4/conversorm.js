//Funcion para habilitar boton
let selectedOption = (option) => {
  let txtRadio = option;
  if (txtRadio == "D") {
    document.getElementById("opcion").innerHTML =
      "Conversión de dólar a bitcoin";
    document.getElementById("cantidad").disabled = false;
  } else if (txtRadio == "B") {
    document.getElementById("opcion").innerHTML =
      "Conversión de bitcoin a dólar";
    document.getElementById("cantidad").disabled = false;
  }
};

//Funcion para habilitar boton
let enableButton = (numero) => {
  let txtNumero = document.getElementById("cantidad").value;
  if (txtNumero > 0) {
    document.getElementById("btnConversor").disabled = false;
  } else {
    document.getElementById("btnConversor").disabled = true;
  }
};

//Función para convertir moneda
let convertirMoneda = (numero) => {
  let txtOpcion = document.getElementById("opcion").textContent;
  if (txtOpcion == "Conversión de dólar a bitcoin") {
    let precio = 0.00004089
    let conversion = numero * precio;
    document.getElementById("resultado").innerHTML =
    "<span>La conversión de $" + numero + " USD a BTC es: </span><span class='respuesta'> " + conversion.toFixed(10) + "BTC</span>";
  } else if (txtOpcion == "Conversión de bitcoin a dólar") {
    let precio = 24452.89
    let conversion = numero * precio;
    document.getElementById("resultado").innerHTML =
    "<span>La conversión de " + numero + " BTC a USD es: </span><span class='respuesta'> $" + conversion.toFixed(2) + "USD</span>";
  }
  clearInputs();
};

let clearInputs = () => {
  document.getElementById("opcion").innerHTML = "";
  document.getElementById("cantidad").value = "";
  document.getElementById("monedad").checked = false;
  document.getElementById("monedab").checked = false;
  document.getElementById("btnConversor").disabled = true;
}
