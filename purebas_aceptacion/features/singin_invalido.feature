Característica: Iniciar Sesion Invalido
    Como usuario de la plataforma comercial digital
    Deseo iniciar sesion 
    Para poder usar e interactuar con el sistema

    Escenario: Datos de ingreso los datos para Iniciar sesion invalidos en usuario
            Dado que ingreso al sistema con credenciales incorrectas en usuario,
            Cuando doy click en el boton de "Iniciar Sesión"
            Y ingreso el nombre incorrecto "usuaario_prueba_incorrecto"
            Y ingreso la contraseña correcta "prueba123"
            Y presiono el boton "Ingresar"
            Entonces veo un mensaje de error "Usuario no encontrado"

    Escenario: Datos de ingreso los datos para Iniciar sesion invalidos en contraseña
            Dado que ingreso al sistema con credenciales incorrectas en contraseña,
            Cuando doy click en el  boton de "Iniciar Sesión"
            Y ingreso el nombre correcto "usuaario_prueba1"
            Y ingreso la contraseña incorrecta "prueba"
            Y presiono el  boton "Ingresar"
            Entonces veo un mensaje  de error "Usuario no encontrado"
