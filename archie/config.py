import os

class Config(object):
    DEBUG = False
    TESTING = False
    LOCAL_DATABASE_URL = 'postgres://archie:Antonine2008@localhost/archie'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_DATABASE_URL)
    WORLD_PROVIDER_ID = 'archie-antonine'
    WORLD_PROVIDER_URL = 'http://vivid-mist-1942.herokuapp.com'
    WORLD_NAME = 'ARCHIE: A Walking Tour on the Antonine Wall'
    WORLD_DESCRIPTION = 'A Walking Tour on the Antonine Wall'
    WORLD_TAGS = 'walking, scotland, antonine, roman, history'
    #    WORLD_LOGO_URL =
    ASSETS_BASE_URL = 'http://s3-eu-west-1.amazonaws.com/antonine-archie'
    WORLD_ICON_URL = '/world/ar-icon.png'
    WORLD_LOGO_URL = '/world/ar-logo.png'
    WORLD_SHORT_NAME = 'ARCHIE'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
