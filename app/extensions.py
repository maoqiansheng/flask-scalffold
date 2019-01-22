"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from celery import Celery


jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
pwd_context = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')
celery = Celery()