//Función para pedir datos por teclado
let pedirDatos = () => {
  //Pedir nombres y edades
  let nombre1 = prompt("Nombre 1:");
  let edad1 = Number(prompt("Edad 1:"));
  let nombre2 = prompt("Nombre 2:");
  let edad2 = Number(prompt("Edad 2:"));
  let nombre3 = prompt("Nombre 3:");
  let edad3 = Number(prompt("Edad 3:"));

  //Determinar la edad mayor
  let maximo = Math.max(edad1, edad2, edad3);

  //Comenzar a dibujar la tabla
  let datos = "<h3>Datos ingresados</h3>";
  datos += "<table>";
  datos += "<tr><th>Nombre</th><th>Edad</th></tr>";
  datos += "<tr><td>" + nombre1 + "</td><td>" + edad1 + "</td></tr>";
  datos += "<tr><td>" + nombre2 + "</td><td>" + edad2 + "</td></tr>";
  datos += "<tr><td>" + nombre3 + "</td><td>" + edad3 + "</td></tr>";
  datos += "</table>";

  if (maximo == edad1) {
    datos += "<span>La persona mayor es: </span><span class='respuesta'>" + nombre1 + "</span>";
  }
  else if (maximo == edad2) {
    datos += "<span>La persona mayor es: </span><span class='respuesta'>" + nombre2 + "</span>";
  }
  else if (maximo == edad3) {
    datos += "<span>La persona mayor es: </span><span class='respuesta'>" + nombre3 + "</span>";
  }

  document.getElementById("resultado").innerHTML = datos;
};
