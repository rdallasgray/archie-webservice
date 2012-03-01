import os

class Config(object):
    DEBUG = False
    TESTING = False
    LOCAL_DATABASE_URL = 'postgres://archie:Antonine2008@localhost/archie'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', LOCAL_DATABASE_URL)
    WORLD_PROVIDER_ID = 'archie-antonine'
    WORLD_PROVIDER_URL = 'http://archie-antonine.org'
    WORLD_NAME = 'ARCHIE: A Walking Tour on the Antonine Wall'
    WORLD_DESCRIPTION = 'A Walking Tour on the Antonine Wall'
    WORLD_TAGS = 'walking, scotland, antonine, roman, history'
    WORLD_LOGO_URL = '/assets/world_logo.png'
    WORLD_ICON_URL = '/assets/world_icon.png'
    WORLD_SHORT_NAME = 'ARCHIE'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
