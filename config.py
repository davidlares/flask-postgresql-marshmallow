class Config:
    pass

# dev environment
class DevelopmentConfig(Config):
    DEBUG = True

# config dictionary
config = {
    'development': DevelopmentConfig
}
