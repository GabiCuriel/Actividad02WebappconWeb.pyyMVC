import web 
import config as config

class Insertt:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        id_p = formulario['id_p'] #almacena el nombre escrito en el input
        nombre_p = formulario['nombre_p']
        existencias = formulario['existencias']
        fecha_c = formulario['fecha_c']
        precio = formulario['precio']

        config.model_productos.insert_productos(id_p,nombre_p,existencias,fecha_c,precio) #llama al metodo insert_datos y le pasa los datos guardados
        raise web.seeother('/productos') #redirecciona al index.html
