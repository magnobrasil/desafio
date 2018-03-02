from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.expProfissional import ExpProfissionalModel

class ExpProfissional(Resource):

    #@jwt_required()
    def get(self, id):
        exp = ExpProfissionalModel.find_by_id(id)
        if exp:
            return exp.json()
        return {'message': 'Exp nao encontrada'}, 404


class ExpProfissionalList(Resource):

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
        return {'exps': list(map(lambda x: x.json(), ExpProfissionalModel.query.all()))}

    def post(self):
        data = ExpProfissionalList.parser.parse_args()
        if ExpProfissionalModel.find_by_descricao(data['descricao']):
            return {'message': "Essa descricao ja existe '{}' .".format(data['descricao'])}, 400

        exp = ExpProfissionalModel(data['descricao'], data['cv_id'])

        try:
            exp.save_to_db()
        except:
            return {"message": "Um erro ocorreu ao salvar a exp profissional"}, 500

        return exp.json(), 201

    
