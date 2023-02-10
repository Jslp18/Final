let a = false;
const divl = document.getElementById('divl');
const divc = document.getElementById('divc');
const divr = document.getElementById('divr')
const btnl = document.getElementById('btn');
const list = document.getElementById('list');
const btn2 = document.getElementById('btn2');
const mode = document.getElementById('mode');
btnl.onclick = function()
{
    btnl.classList.toggle('activo');
    divl.classList.toggle('activo');
    divc.classList.toggle('activo');
    divr.classList.toggle('activo');
    list.classList.toggle('activo');
    btn2.classList.toggle('activo');
    if(a) {
        a = false;
        mode.innerHTML = "MODO CLARO";
    }
    else {
        a = true;
        mode.innerHTML = "MODO OSCURO";
    }
}