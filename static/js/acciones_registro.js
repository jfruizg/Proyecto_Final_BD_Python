function RegistroAdmin() {
    document.getElementById('registro_admin').style.display = 'block';
    document.getElementById('registro_cliente').style.display = 'none';
    document.getElementById('registro_empleado').style.display = 'none';
}

function RegsitroEmpleado() {
    document.getElementById('registro_admin').style.display = 'none';
    document.getElementById('registro_cliente').style.display = 'none';
    document.getElementById('registro_empleado').style.display = 'block';
}

function RegistroCliente() {
    document.getElementById('registro_admin').style.display = 'none';
    document.getElementById('registro_cliente').style.display = 'block';
    document.getElementById('registro_empleado').style.display = 'none';
}
