import web 
import config as config 

class Deletee: 
    def __init__(self):
        pass

    def GET(self, id_p):
        productos = config.model_productos.select_id_p(id_p) #selecciona el registro que coincida con nombre
        return config.render.delete(productos) #envia el resgistro y renderiza delete.html

    def POST(self, id_p):
        formulario = web.input() #crea un objeto formulario con los datos enviados con el formulario 
        id_p = formulario['id_p'] #obtiene el nombre almacenado en el formulario
        config.model_productos.delete_productos(id_p) #borra el registro del nombre seleccionado
        raise web.seeother('/productos') #renderiza a raiz
        