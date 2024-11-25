from flask_mysqldb import MySQL

def inicializar_bd(app):
    # Configuración de MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'proyecto'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    return MySQL(app)