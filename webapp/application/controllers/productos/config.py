import web #Importa la libreria web.py
import application.models.model_productos as model_productos #Importa el modelo_productos

render = web.template.render('application/views/productos/', base='master') #configura la ubicacion de las vistas
