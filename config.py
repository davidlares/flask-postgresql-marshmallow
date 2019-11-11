class Config:
    pass

# dev environment
class DevelopmentConfig(Config):
    DEBUG = True
    # ORM setup
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# config dictionary
config = {
    'development': DevelopmentConfig
}
