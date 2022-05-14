var google= document.getElementById("google");

google.addEventListener("mouseenter" ,()=>{
    google.classList.remove("boton-seguir");
    google.classList.add("boton-seguir-arriba");
})

google.addEventListener("mouseleave" ,()=>{
    google.classList.add("boton-seguir");
    google.classList.remove("boton-seguir-arriba");
})