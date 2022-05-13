import os


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/sixty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email config_options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'davinci.monalissa3@gmail.com'
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'The Pitcher'
    SENDER_EMAIL = 'davinci.monalissa3@gmail.com'


class ProdConfig(Config):
    """
    production configuration child class
    """

    pass


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
