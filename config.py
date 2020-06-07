class Config(object):
    MAIL_SERVEUR = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'latartefrancaise@gmail.com'
    MAIL_PASSWORD = '4XaE1X1j0J9maXXlcf'
    MAIL_DEBUG = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    MYSQL = {
        'user': 'root',
        'pw': '',
        'db': 'np2',
        'host': 'localhost',
        'port': '3306',
    }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % MYSQL
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
