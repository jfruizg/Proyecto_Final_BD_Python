/*Menu lateral admin*/

/*Accion mostrar y ocultar empleado*/

function Function_Empleado() {
    cerrar_pestana
    var x = document.getElementById("info-empleado");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function Function_admin() {
    var x = document.getElementById("info-admin");
    cerrar_pestana(x)
    if (x.style.display === "none") {
        x.style.display = "block";
    }else{
        cerrar_pestana(x)
    }
}


/*Accion mostrar y ocultar cliente*/
function Function_cliente() {
    var x = document.getElementById("info-Cliente");
    cerrar_pestana(x)
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

/*Accion mostrar y ocultar Libros*/
function Function_libro() {
    var x = document.getElementById("info-libro");
    cerrar_pestana(x)
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
/*Accion mostrar y ocultar Peliculas*/
function Function_pelicula() {
    var x = document.getElementById("info-pelicula");
    cerrar_pestana(x)
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function cerrar_pestana(ene){
    ene.style.display = "none";
}
