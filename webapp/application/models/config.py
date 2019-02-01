import web
"""
parametros de configuracion para conectarse a una base de datos 
MySQL O MariaDB
"""
DB = web.database(
    dbn='mysql', #motor de base de datos
    host='localhost', #ruta del server
    db='ria_iniciales', #nombre de la base de datos
    user='ria', #usuario de la base de datos
    pw='ria.2019', #password del usuario
    port=3306 #puerto de mariadb
)
