//Función para crear tabla dinámica
let crearTabla = () => {
    let i, j;
    let fila = Number(prompt("Escriba el número de filas"));
    let colum = Number(prompt("Escriba el número de columnas"));
    let resultado = fila * colum;
    let tablaDin = '<table>'; //Se comienza a llenar la tabla
    for (i = 0; i < fila; i++) {
        tablaDin += "<tr>" //Abrir fila
        for (j = 0; j < colum; j++) {
            tablaDin += "<td>" + resultado //Se ingresan los números
            resultado--;
            tablaDin += "</td>" //Cerrar columna
        }
        tablaDin += "</tr>" //Cerrar fila
    }
    tablaDin += "</table>"; //Cerrar tabla
    document.getElementById("resultado").innerHTML = tablaDin; //Imprimir tabla
};