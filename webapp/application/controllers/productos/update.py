import web 
import config as config 

class Updatee:
    def __init__(self):
        pass
    
    def GET(self, id_p):
        productos =config.model_productos.select_id_p(id_p) #selecciona el registro que coincida con nombre
        return config.render.update(productos) #envia el registro update.html

    def POST(self, nombre_p):
        formulario = web.input() #almacena los datos del formulario web
        id_p = formulario['id_p'] #almacena el nombre de input email
        nombre_p = formulario['nombre_p']
        existencias = formulario['existencias']
        fecha_c = formulario['fecha_c']
        precio = formulario['precio']

        config.model_productos.update_productos(id_p,nombre_p,existencias,fecha_c,precio) #actualiza los valores
        raise web.seeother('/productos') #redirecciona el index