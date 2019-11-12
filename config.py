class Config:
    pass

# dev environment
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# config dictionary
config = {
    'test': TestConfig,
    'development': DevelopmentConfig
}
