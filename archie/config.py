class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///archie.db'
    WORLD_PROVIDER_ID = 'archie-antonine'
    WORLD_PROVIDER_URL = 'http://archie-antonine.org'
    WORLD_NAME = 'ARCHIE: A Walking Tour on the Antonine Wall'
    WORLD_DESCRIPTION = 'Walking tours on the Antonine Wall'
    WORLD_TAGS = 'walking, scotland, antonine, roman, history'
    WORLD_LOGO_URL = '/assets/world_logo.png'
    WORLD_ICON_URL = '/assets/world_icon.png'
    WORLD_SHORT_NAME = 'ARCHIE'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
