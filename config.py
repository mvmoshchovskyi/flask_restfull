class Config:
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:wer45012@localhost/data_rest'
    SECRET_KEY = ' very secret key'
