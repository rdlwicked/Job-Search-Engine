import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///your-database-file.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
