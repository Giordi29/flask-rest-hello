class Config:
    SQLALCHEMY_DATABASE_URI = 'qlite:///starwars.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ecret_key_here'  