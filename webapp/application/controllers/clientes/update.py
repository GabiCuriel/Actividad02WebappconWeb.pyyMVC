import web 
import config as config 

class Update:
    def __init__(self):
        pass
    
    def GET(self, nombre_c):
        clientes =config.model_clientes.select_nombre_c(nombre_c) #selecciona el registro que coincida con nombre
        return config.render.update(clientes) #envia el registro update.html

    def POST(self, email):
        formulario = web.input() #almacena los datos del formulario web
        nombre_c = formulario['nombre_c'] #almacena el nombre de input email
        apepat_c = formulario['apepat_c']
        apemat_c = formulario['apemat_c']
        telefono_c = formulario['telefono_c']
        email = formulario['email'] #almacena el email del input password

        config.model_clientes.update_clientes(nombre_c,apepat_c,apemat_c,telefono_c,email) #actualiza los valores
        raise web.seeother('/clientes') #redirecciona el index