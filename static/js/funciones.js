function modalUsuario(url, first_name){
    document.getElementById('form_eliminar').action = url;
    document.getElementById('modal_body').innerHTML = `¿Deseas eliminar el usuario' + ${first_name} + ?`; 
}

$("#id_estado").on('change',function () { 
    var token = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "post",
        url: `/users/municipios/`,
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
