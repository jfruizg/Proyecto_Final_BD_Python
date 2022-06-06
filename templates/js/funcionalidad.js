/*redireccion de registro a principal HTML*/
function volver(){
    location.href = "login.html";
}
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