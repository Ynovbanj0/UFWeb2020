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

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
