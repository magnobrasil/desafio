from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.artigo import ArtigoModel

class Artigo(Resource):

    @jwt_required()
    def get(self, id):
        exp = ArtigoModel.find_by_id(id)
        if exp:
            return exp.json()
        return {'message': 'Exp nao encontrada'}, 404

    def delete(self, name):
        artigo = ArtigoModel.find_by_descricao(descricao)
        if artigo:
            artigo.delete_from_db()

        return {'message': 'Artigo deletado'}

    def put(self, descricao):
        data = Artigo.parser.parse_args()

        artigo = ArtigoModel.find_by_descricao(descricao)

        if artigo:
            artigo.descricao = data['descricao']

        artigo.save_to_db()

        return exp.json()

class ArtigoList(Resource):

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
        return {'artigos': list(map(lambda x: x.json(), ArtigoModel.query.all()))}

    def post(self):
        data = ArtigoList.parser.parse_args()
        if ArtigoModel.find_by_descricao(data['descricao']):
            return {'message': "Esse artigo ja existe '{}' .".format(descricao)}, 400

        artigo = ArtigoModel(data['descricao'], data['cv_id'])

        try:
            artigo.save_to_db()
        except:
            return {"message": "Um erro ocorreu ao salvar o artigo"}, 500

        return artigo.json(), 201
