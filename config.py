class Config(object):
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    MYSQL = {
        'user': 'root',
        'pw': '',
        'db': 'np2',
        'host': 'localhost',
        'port': '3306',
    }
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % MYSQL
    MAIL_SERVEUR = 'smtp.gmail.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'nopay.noplay2020@gmail.com'
    MAIL_PASSWORD = 'Bobo1234'
    MAIL_DEFAULT_SENDER = 'nopay.noplay2020@gmail.com'
    MAIL_MAX_EMAILS = 2
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
