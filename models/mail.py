from flask_mail import Mail

def configurar_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'fullweb10@gmail.com'
    app.config['MAIL_PASSWORD'] = 'zrgd cwow fexh ykgw'
    app.config['MAIL_DEFAULT_SENDER'] = 'fullweb10@gmail.com'
    return Mail(app)