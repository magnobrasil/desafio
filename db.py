from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.text_factory = str
