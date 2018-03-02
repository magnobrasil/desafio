from db import db

class ArtigoModel(db.Model):
    __tablename__ = 'artigo'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(80))

    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'))
    cv = db.relationship('CvModel')

    def __init__(self, descricao, cv_id):
        self.descricao = descricao
        self.cv_id = cv_id

    def json(self):
        return {'id':self.id,'descricao': self.descricao}

    @classmethod
    def find_by_descricao(cls, descricao):
        return cls.query.filter_by(descricao=descricao).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        id =  db.session.add(self)
        db.session.commit()
        return id
       

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
