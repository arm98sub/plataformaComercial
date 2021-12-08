from behave import when, then, given
import time


@given(u'que ingreso al sistema con credenciales incorrectas en usuario,')
def step_impl(context):
    pass
    
@when(u'doy click en el boton de "Iniciar Sesión"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div/div/div[2]/ul/li/a[1]').click()
    time.sleep(4)

@when(u'ingreso el nombre incorrecto "{prueba}"')
def step_impl(context, prueba):
    context.driver.find_element_by_id('id_username').send_keys(prueba)
    time.sleep(1)

@when(u'ingreso la contraseña correcta "{contra}"')
def step_impl(context,contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(1)

@when(u'presiono el boton "Ingresar"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/section/div/div/div[1]/div/form/div[3]/button').click()
    time.sleep(2)
    
@then(u'veo un mensaje de error "Usuario no encontrado"')
def step_impl(context):
    assert context.driver.find_element_by_xpath('/html/body/div[3]/p').text == "Usuario no encontrado"
    



@given(u'que ingreso al sistema con credenciales incorrectas en contraseña,')
def step_impl(context):
    pass
    
@when(u'doy click en el  boton de "Iniciar Sesión"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div/div/div[2]/ul/li/a[1]').click()
    time.sleep(4)

@when(u'ingreso el nombre correcto "{prueba}"')
def step_impl(context, prueba):
    context.driver.find_element_by_id('id_username').send_keys(prueba)
    time.sleep(1)

@when(u'ingreso la contraseña incorrecta "{contra}"')
def step_impl(context,contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(1)

@when(u'presiono el  boton "Ingresar"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/section/div/div/div[1]/div/form/div[3]/button').click()
    time.sleep(2)
    
@then(u'veo un mensaje  de error "Usuario no encontrado"')
def step_impl(context):
    assert context.driver.find_element_by_xpath('/html/body/div[3]/p').text == "Usuario no encontrado"
    
