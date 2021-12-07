from behave import when, then, given
import time


@given(u'que ingreso al sistema para crear cuenta de empresa,')
def step_impl(context):
    pass
    
@when(u'doy click en "REGISTRAR" para crear cuenta de empresa')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div/div/div[2]/ul/li/a[2]').click()
    time.sleep(2)

@when(u'doy click en "Crear Cuenta Empresarial"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/p/a').click()
    time.sleep(2)
    
@when(u'ingreso el nombre de empresa "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element_by_id('id_first_name').send_keys(nombre)
    time.sleep(2)
    
    
@when(u'ingreso el nombre de usuario empresa "{nombreU}"')
def step_impl(context, nombreU):
    context.driver.find_element_by_id('id_username').send_keys(nombreU)
    time.sleep(2)

@when(u'ingreso la contraseña de empresa "{contra}"')
def step_impl(context,contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(2)

@when(u'ingreso la verifico la contraseña de empresa "{contra2}"')
def step_impl(context,contra2):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[4]/div/input').send_keys(contra2)
    time.sleep(2)
    
@when(u'ingreso la el coreo electronico de empresa "{correo}"')
def step_impl(context,correo):
    context.driver.find_element_by_id('id_email').send_keys(correo)
    time.sleep(2)

@when(u'selecciono el estado de empresa Zacatecas')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/div/div').click()
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/div/div/ul/li[2]').click()
    time.sleep(2)

@when(u'selecciono el municipio de empresa Villa Gonzalez')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[8]/div/div').click()
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[8]/div/div/ul/li[2]').click()
    time.sleep(2)

@when(u'ingreso la direccion "{direccion}"')
def step_impl(context,direccion):
    context.driver.find_element_by_id('id_direccion').send_keys(direccion)
    time.sleep(2)


@when(u'ingreso el telefono "{telefono}"')
def step_impl(context,telefono):
    context.driver.find_element_by_id('id_telefono').send_keys(telefono)
    time.sleep(2)

@when(u'doy click en el botón "Crear Cuenta"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[12]/button').click()
    time.sleep(2)
    
@then(u'me dirijo a la pantalla de inicio de sesion')
def step_impl(context):
    context.driver.get('http://192.168.33.10:8000/usuarios/login/')
    time.sleep(2)
