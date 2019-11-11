class Config:
    pass

# dev environment
class DevelopmentConfig(Config):
    DEBUG = True
    # ORM setup
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    DEBUG = False
    # ORM setup
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# config dictionary
config = {
    'development': DevelopmentConfig,
    'test': TestConfig
}
