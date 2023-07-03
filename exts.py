from flask_sqlalchemy import SQLAlchemy
import hashlib
import config

db = SQLAlchemy()


def encrypt(content):
    content += config.salt
    content = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return content
