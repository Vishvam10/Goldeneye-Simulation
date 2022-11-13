import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    TESTING = None
    SQLITE_DB_DIR = None
    SQLALCHEMY_DB_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    # SMTP_SERVER_HOST = "localhost"
    # SMTP_SERVER_PORT = 25
    # SENDER_ADDRESS = "vishvam@gmail.com"
    # SENDER_PASSWORD = ""
    # CELERY_BROKER_URL = "redis://localhost:6379/1"
    # CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    # CACHE_TYPE = "RedisCache"
    # CACHE_REDIS_HOST = "localhost"
    # CACHE_REDIS_PORT = 6379


class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(SQLITE_DB_DIR, "db.sqlite3")
    DEBUG = True
    TESTING = False
    CORS_HEADERS = "Content-Type"
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEDIA_FOLD = os.getcwd() + '\media'
    MEDIA_FOLDER = os.path.join(APP_ROOT, MEDIA_FOLD)
    # CACHE_TYPE = "RedisCache"
    # CACHE_REDIS_HOST = "localhost"
    # CACHE_REDIS_PORT = 6379


class LocalTestingConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(SQLITE_DB_DIR, "test_db.sqlite3")
    DEBUG = True
    TESTING = True
    CORS_HEADERS = "Content-Type"
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEDIA_FOLD = os.getcwd() + '\media'
    MEDIA_FOLDER = os.path.join(APP_ROOT, MEDIA_FOLD)


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
    CORS_HEADERS = "Content-Type"
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEDIA_FOLD = os.getcwd() + '\media'
    MEDIA_FOLDER = os.path.join(APP_ROOT, MEDIA_FOLD)
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", None)
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", None)
