import web
import config as config

class View:
    def __init__(self):
        pass

    def GET(self, nombre_c):
        clientes = config.model_clientes.select_nombre_c(nombre_c) #selecciona el registro que coincisa con nombre
        return config.render.view(clientes) #Envia el registro y renderiza view.html 
