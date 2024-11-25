const seccionesOcultas = document.querySelectorAll(".hidden");

const observer = new IntersectionObserver((entradas)=>{
    entradas.forEach(entrada =>{
        entrada.target.classList.toggle("mostrar",entrada.isIntersecting)
    })
})

seccionesOcultas.forEach((seccion)=>observer.observe(seccion))