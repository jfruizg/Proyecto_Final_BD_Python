/*redireccion de registro a principal HTML*/
function volver(){
    location.href = "Ventana_Principal.html";
}

/*redireccion de Cerrar Sesion a principal HTML*/
function cerrarsesion(){
    location.href = "Ventana_Principal.html";
}

/*Mostrar formulario Empleado*/
function cliente() {
    var x = document.getElementById("tabla_cliente");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
/*Mostrar Formulario Administrador*/
function empleado() {
    var x = document.getElementById("tabla_Empleado");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
/*Mostrar formulario Empleado*/
function administrador() {
    var x = document.getElementById("tabla_admin");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}