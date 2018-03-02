from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.cv import Cv, CvList
from resources.artigo import Artigo, ArtigoList
from resources.curso import Curso, CursoList
from resources.expProfissional import ExpProfissional, ExpProfissionalList
import sys

reload(sys)
sys.setdefaultencoding("UTF8")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'EiEiO'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Cv, '/cv/<string:id>')
api.add_resource(CvList, '/cvs')

api.add_resource(Artigo, '/artigo/<string:id>')
api.add_resource(ArtigoList, '/artigos')

api.add_resource(Curso, '/curso/<string:id>')
api.add_resource(CursoList, '/cursos')

api.add_resource(ExpProfissional, '/experiencia/<string:id>')
api.add_resource(ExpProfissionalList, '/experiencias')


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
