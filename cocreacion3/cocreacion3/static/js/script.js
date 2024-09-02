// Espera a que el documento HTML esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  // Selecciona todos los elementos HTML con la clase "gallery"
  const galleries = document.querySelectorAll(".gallery");

  // Por cada galería encontrada, realiza las siguientes acciones
  galleries.forEach(function(gallery) {
      // Dentro de cada galería, selecciona todos los elementos de imagen (img)
      const images = gallery.querySelectorAll("img");
      // Variable para llevar el seguimiento del índice actual de la imagen mostrada
      let currentIndex = 0;

      // Función para mostrar una imagen específica según su índice
      function showImage(index) {
          // Oculta todas las imágenes estableciendo su opacidad a 0
          images.forEach(img => {
              img.style.opacity = 0;
          });
          // Muestra la imagen con el índice proporcionado estableciendo su opacidad a 1
          images[index].style.opacity = 1;
      }

      // Agrega un evento de clic a la galería
      gallery.addEventListener("click", function() {
          // Avanza al siguiente índice de imagen (circular, volviendo al principio si se alcanza el final)
          currentIndex = (currentIndex + 1) % images.length;
          // Muestra la imagen actualizada
          showImage(currentIndex);
      });

      // Configura un intervalo para cambiar automáticamente la imagen cada 3 segundos
      setInterval(function() {
          // Avanza al siguiente índice de imagen (circular)
          currentIndex = (currentIndex + 1) % images.length;
          // Muestra la imagen actualizada
          showImage(currentIndex);
      }, 3000); // 3000 milisegundos = 3 segundos
  });
});
  
  