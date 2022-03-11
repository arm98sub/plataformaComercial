function modalUsuario(url, first_name){
    document.getElementById('form_eliminar').action = url;
    document.getElementById('modal_body').innerHTML = `¿Deseas eliminar el usuario' + ${first_name} + ?`; 
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