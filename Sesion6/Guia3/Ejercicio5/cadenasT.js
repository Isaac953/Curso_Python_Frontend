//Función para convertir moneda
let concatenarCadena = () => {
    let cadenaConcat = ""
    do {
        let cadena = prompt("Introduce una cadena");
        if (cadenaConcat == "") {
            cadenaConcat = cadenaConcat + cadena;
        }
        else {
            cadenaConcat = cadenaConcat + "-" + cadena;
        }
    } while (confirm("Desea seguir?"));

    document.getElementById("resultado").innerHTML =
    "<span class='respuesta'>" + cadenaConcat + "</span>";
};