const seccionesOcultas = document.querySelectorAll(".hidden");

const observer = new IntersectionObserver((entradas)=>{
    entradas.forEach(entrada =>{
        entrada.target.classList.toggle("mostrar",entrada.isIntersecting)
    })
})

seccionesOcultas.forEach((seccion)=>observer.observe(seccion))

const formNuevaClave = document.querySelector(".formNuevaClave")
const btnOlvidarContraseña = document.querySelector(".btn-olvidar-contraseña")
const contenedorNuevaClave = document.getElementById("contenedorNuevaClave")
const btnCerrar = document.querySelector(".btnCerrar")
const btnEnviarClaveNueva = document.querySelector(".btnEnviarClaveNueva")

btnOlvidarContraseña.addEventListener("click",function(){
    contenedorNuevaClave.style.display = "flex"
})

btnCerrar.addEventListener("click",function(){
    contenedorNuevaClave.style.display = "none"
})