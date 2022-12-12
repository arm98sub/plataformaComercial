function modalUsuario(url, first_name){
    document.getElementById('form_eliminar').action = url;
    document.getElementById('modal_body').innerHTML = `¿Deseas eliminar el usuario' + ${first_name} + ?`; 
}

function modalProducto(url, nombre){
  document.getElementById('form_eliminarp').action = url;
  document.getElementById('modal_body').innerHTML = `¿Deseas eliminar el producto' + ${nombre} + ?`; 
}

$("#id_estado").on('change',function () { 
    var token = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "post",
        url: `/user/municipios/`,
        data:{'id':this.value, 'csrfmiddlewaretoken':token},
        success: function (response) {
            var html = ""
            if (response[0].hasOwnProperty('error')){
                html += `<option value="0">${response[0].error}</option>"`;

            }
            else{
                $.each(response, function (llave, valor) { 
                 html += `<option value="${valor.id}">${valor.nombre}</option>"`;
                });
                //console.log(response)
            }
            $("#id_municipio").html(html);
        },
        error: function(param){
            console.log('Error en la peticion');
        }
    });
});

jQuery(function ($) {

    $(".sidebar-dropdown > a").click(function() {
  $(".sidebar-submenu").slideUp(200);
  if (
    $(this)
      .parent()
      .hasClass("active")
  ) {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .parent()
      .removeClass("active");
  } else {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .next(".sidebar-submenu")
      .slideDown(200);
    $(this)
      .parent()
      .addClass("active");
  }
});

$("#close-sidebar").click(function() {
  $(".page-wrapper").removeClass("toggled");
});
$("#show-sidebar").click(function() {
  $(".page-wrapper").addClass("toggled");
});


   
   
});

const myCarousel = document.getElementById("carouselIndex");
const carouselIndicators = myCarousel.querySelectorAll(
  ".carousel-indicators button span"
);
let intervalID;

const carousel = new bootstrap.Carousel(myCarousel);

window.addEventListener("load", function () {
  fillCarouselIndicator(1);
});

myCarousel.addEventListener("slide.bs.carousel", function (e) {
  let index = e.to;
  fillCarouselIndicator(++index);
});

function fillCarouselIndicator(index) {
  let i = 0;
  for (const carouselIndicator of carouselIndicators) {
    carouselIndicator.style.width = 0;
  }
  clearInterval(intervalID);
  carousel.pause();

  intervalID = setInterval(function () {
    i++;

    myCarousel.querySelector(".carousel-indicators .active span").style.width =
      i + "%";

    if (i >= 100) {
      // i = 0; -> just in case
      carousel.next();
    }
  }, 50);
}

