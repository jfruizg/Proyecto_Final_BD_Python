/*Menu lateral admin*/
const toggle = document.querySelector(".toggle")
const menuDashboard = document.querySelector(".menu-dashboard")
const iconmenu = document.querySelector("i")
const enlacesMenu = document.querySelector(".enlace")

toggle.addEventListener("click", ()=> {
    menuDashboard.classList.toggle("open");

    if(iconmenu.classList.contains("bx-menu")){
        iconmenu.classList.replace("bx-menu", "bx,x")
    }else{
        iconmenu.classList.replace("bx-x", "bx-menu")
    }
})

enlacesMenu.forEach(enlace => {
    enlace.addEventListener("click", () =>{
        menuDashboard.classList.add("open")
        iconmenu.classList.replace("bx-menu", "bx-x")
    })
});
/*Accion mostrar y ocultar empleado*/

function Function_Empleado() {
    var x = document.getElementById("info-empleado");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
/*Accion mostrar y ocultar cliente*/
function Function_cliente() {
    var x = document.getElementById("info-Cliente");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

/*Accion mostrar y ocultar Libros*/
function Function_libro() {
    var x = document.getElementById("info-libro");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
/*Accion mostrar y ocultar Peliculas*/
function Function_pelicula() {
    var x = document.getElementById("info-pelicula");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
