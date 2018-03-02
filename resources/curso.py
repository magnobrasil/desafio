from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.curso import CursoModel

class Curso(Resource):
    #@jwt_required()
    def get(self, id):
        exp = CursoModel.find_by_id(id)
        if exp:
            return exp.json()
        return {'message': 'Curso nao encontrado'}, 404

    def delete(self, id):
        curso = CursoModel.find_by_descricao(descricao)
        if curso:
            curso.delete_from_db()

        return {'message': 'curso deletado'}

    def put(self, id):
        data = CursoModel.parser.parse_args()

        curso = CursoModel.find_by_descricao(descricao)

        if curso:
            curso.descricao = data['descricao']

        curso.save_to_db()

        return exp.json()

class CursoList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('descricao',
        type=str,
        required=True,
        help="Este campo nao pode ficar em branco."
    )
    parser.add_argument('cv_id',
        type=int,
        required=True,
        help="Toda exp profissional precisa de um cv."
    )

    def get(self):
        return {'cursos': list(map(lambda x: x.json(), CursoModel.query.all()))}

    def post(self):
        data = CursoList.parser.parse_args()

        if CursoModel.find_by_descricao(data['descricao']):
            return {'message': "Essa descricao ja existe '{}' .".format(descricao)}, 400
       
        curso = CursoModel(data['descricao'], data['cv_id'])
        try:
            curso.save_to_db()
        except:
            return {"message": "Um erro ocorreu ao salvar o curso"}, 500

        return curso.json(), 201
