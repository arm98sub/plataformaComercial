from behave import when, then, given
import time


@given(u'que ingreso al sistema con credenciales correctas,')
def step_impl(context):
    pass
    
@when(u'doy click en "Iniciar Sesión"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div/div/div[2]/ul/li/a[1]').click()
    time.sleep(4)

@when(u'ingreso el nombre con "{prueba}"')
def step_impl(context, prueba):
    context.driver.find_element_by_id('id_username').send_keys(prueba)
    time.sleep(1)

@when(u'ingreso la contraseña "{contra}"')
def step_impl(context,contra):
    context.driver.find_element_by_id('id_password').send_keys(contra)
    time.sleep(1)


@when(u'presiono el botón "Ingresar"')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[3]/section/div/div/div[1]/div/form/div[3]/button').click()
    time.sleep(2)
    
@then(u'ingreso a la pantalla de inicio')
def step_impl(context):
    context.driver.get('http://127.0.0.1:8000')
