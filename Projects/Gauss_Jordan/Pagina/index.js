// Lógica para ocultar pantalla de inicio y mostrar contenido principal
const pantallaInicio = document.getElementById("pantalla-inicio");
const contenidoPrincipal = document.getElementById("contenido-principal");
const btnEmpezar = document.getElementById("btn-empezar");

btnEmpezar.addEventListener("click", function () {
  // Ocultar pantalla de inicio
  pantallaInicio.classList.add("oculta");
  // Mostrar contenido principal
  contenidoPrincipal.classList.add("visible");
});

const btnOperation = document.getElementById("btn_operation");

btnOperation.addEventListener("click", (e) => {
  console.log("hola");
  contenidoPrincipal.classList.toggle("agrandar")
});
