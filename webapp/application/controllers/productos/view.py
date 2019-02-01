import web
import config as config

class Vieww:
    def __init__(self):
        pass

    def GET(self, id_p):
        productos = config.model_productos.select_id_p(id_p) #selecciona el registro que coincisa con nombre
        return config.render.view(productos) #Envia el registro y renderiza view.html 
