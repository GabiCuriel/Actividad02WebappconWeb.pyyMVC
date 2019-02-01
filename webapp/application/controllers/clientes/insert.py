import web 
import config as config

class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        nombre_c = formulario['nombre_c'] #almacena el nombre escrito en el input
        apepat_c = formulario['apepat_c']
        apemat_c = formulario['apemat_c']
        telefono_c = formulario['telefono_c']
        email = formulario['email']

        config.model_clientes.insert_clientes(nombre_c,apepat_c,apemat_c,telefono_c,email) #llama al metodo insert_datos y le pasa los datos guardados
        raise web.seeother('/clientes') #redirecciona al index.html
