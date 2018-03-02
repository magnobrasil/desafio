from flask_restful import Resource, reqparse
from models.cv import CvModel
from flask_jwt import jwt_required
import sys

class Cv(Resource):
    #@jwt_required()
    def get(self, id):
        cv = CvModel.find_by_id(id)
        if cv:
            return cv.json()
        return {'message': 'Cv nao encontrado'}, 404


    def delete(self, id):
        cv = CvModel.find_by_id(id)
        if cv:
            cv.delete_from_db()

        return {'message': 'Cv deletado'}

class CvList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nome',
        type=str,
        required=True,
        help="nome"
    )
    parser.add_argument('endereco',
        type=str,
        required=True,
        help="endereco errado"
    )

    parser.add_argument('experienciaResumo',
        type=str,
        required=True,
        help="experienciaResumo"
    )

    parser.add_argument('formacaoAcademica',
        type=str,
        required=True,
        help="formacaoAcademica"
    )



    def get(self):
        return {'cvs': list(map(lambda x: x.json(), CvModel.query.all()))}

    def post(self):

        data = CvList.parser.parse_args()

        if CvModel.find_by_nome(data['nome']):
            return {'message': "Um cv com este nome '{}' ja existe.".format(nome)}, 400

    

        cv = CvModel(str(data['nome']),
        str(data['endereco']),
        str(data['experienciaResumo']),
        str(data['formacaoAcademica']))
        try:
            cv.save_to_db()
        except Exception as e:
            return {"message": "Um erro ocorreu ao salvar o CV." + str(e)}, 500

        return cv.json(), 201
