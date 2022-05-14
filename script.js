var engranaje= document.getElementById("engranaje");

engranaje.addEventListener("mouseenter" ,()=>{
    engranaje.classList.remove("estable");
    engranaje.classList.add("rotado");
})

engranaje.addEventListener("mouseleave" ,()=>{
    engranaje.classList.add("estable");
    engranaje.classList.remove("rotado");
})

var pin= document.getElementById("pin");

pin.addEventListener("mouseenter" ,()=>{
    pin.classList.remove("img-location");
    pin.classList.add("img-location-hop");
})

pin.addEventListener("mouseleave" ,()=>{
    pin.classList.add("img-location");
    pin.classList.remove("img-location-hop");
})

var ajustes= document.getElementById("ajustes");

ajustes.addEventListener("click" ,()=>{
    alert("Haz hecho click al boton de ajustes");
})

var Jorge= document.getElementById("Jorge");

Jorge.addEventListener("dblclick" ,()=>{
    Jorge.classList.toggle("img-user");
    Jorge.classList.toggle("img-user-expand");
})

