from db import db

class CvModel(db.Model):
    __tablename__ = 'cv'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(500))
    endereco = db.Column(db.String(500))
    experienciaResumo = db.Column(db.String(500))
    formacaoAcademica = db.Column(db.String(500))

    experienciaProfissionais = db.relationship('ExpProfissionalModel', lazy='dynamic')
    artigos = db.relationship('ArtigoModel', lazy='dynamic')
    cursos = db.relationship('CursoModel', lazy='dynamic')

    def __init__(self, nome,endereco, experienciaResumo,formacaoAcademica):
        self.nome = nome
        self.endereco = endereco
        self.experienciaResumo = experienciaResumo
        self.formacaoAcademica = formacaoAcademica

    def json(self):
        return {
                'id':self.id,
                'nome': self.nome, 
               'endereco': self.endereco, 
               'experienciaResumo': self.experienciaResumo,
               'formacaoAcademica': self.formacaoAcademica,  
               'artigos': [artigo.json() for artigo in self.artigos.all()],
               'cursos': [curso.json() for curso in self.cursos.all()],
               'expProfissionais': [exp.json() for exp in self.experienciaProfissionais.all()]}

    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
       

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
