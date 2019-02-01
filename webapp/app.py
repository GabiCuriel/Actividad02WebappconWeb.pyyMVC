import web 

urls= (
    '/clientes', 'application.controllers.clientes.index.Index',
    '/insert', 'application.controllers.clientes.insert.Insert',
    '/update/(.*)', 'application.controllers.clientes.update.Update',
    '/delete/(.*)', 'application.controllers.clientes.delete.Delete',
    '/view/(.*)', 'application.controllers.clientes.view.View',
    '/productos', 'application.controllers.productos.index.Index',
    '/insertp', 'application.controllers.productos.insert.Insertt',
    '/updatep/(.*)', 'application.controllers.productos.update.Updatee',
    '/deletep/(.*)', 'application.controllers.productos.delete.Deletee',
    '/vieww/(.*)', 'application.controllers.productos.view.Vieww'
)

if __name__ == '__main__':
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
    