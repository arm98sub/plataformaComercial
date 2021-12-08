from behave import when, then, given
import time


@given(u'que ingreso al sistema,')
def step_impl(context):
    pass
    
@when(u'doy click en "REGISTRAR"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div/div/div[2]/ul/li/a[2]').click()
    time.sleep(2)

@when(u'ingreso el nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_id('id_first_name').send_keys(nombre)
    time.sleep(2)

@when(u'ingreso el nombre de usuario "{nombreU}"')
def step_impl(context, nombreU):
    context.driver.find_element_by_id('id_username').send_keys(nombreU)
    time.sleep(2)   

@when(u'ingreso la contraseña con "{contra}"')
def step_impl(context,contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(2)

@when(u'ingreso la verifico la contraseña "{contra2}"')
def step_impl(context,contra2):
    context.driver.find_element_by_id('id_password2').send_keys(contra2)
    time.sleep(2)
    
@when(u'ingreso la el coreo electronico "{correo}"')
def step_impl(context,correo):
    context.driver.find_element_by_id('id_email').send_keys(correo)
    time.sleep(2)

@when(u'presiono el botón "Crear Cuenta"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/button').click()
    time.sleep(2)
    
    
@then(u'ingreso a la pantalla de inicio de sesion')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000/usuarios/login/')
    time.sleep(2)
