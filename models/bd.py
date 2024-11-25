import os
from flask_mysqldb import MySQL

def inicializar_bd(app):
    # Configuración de MySQL utilizando variables de entorno
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    return MySQL(app)