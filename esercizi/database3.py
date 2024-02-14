'''
Creare un database SQLite con una due tabelle: Studenti, Esami e Classi e stabilire una relazione tra le tabelle.
Esegui una query per recuperare lo studente che in italiano ha voto superiore a 18.
Nota: utilizza SQLAlchemy per creare il database.
'''
from sqlalchemy import and_, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class Studenti(Base):
    __tablename__ = 'studenti'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cognome = Column(String)
    esami = relationship("Esami", back_populates="studente")
    classi = relationship("Classi", back_populates="studente")

    def __repr__(self):
        return "<Studenti(nome='%s', cognome='%s', esami='%s', classi='%s')>" % (self.nome, self.cognome, self.esami, self.classi)
    
class Esami(Base):
    __tablename__ = 'esami'
    id = Column(Integer, primary_key=True)
    studente_id = Column(Integer, ForeignKey('studenti.id'))
    materia = Column(String)
    voto = Column(Integer)
    studente = relationship("Studenti", back_populates="esami")
    
    def __repr__(self):
        return "<Esami(studente_id='%s', materia='%s', voto='%s')>" % (self.studente_id, self.materia, self.voto)
    
class Classi(Base):
    __tablename__ = 'classi'
    id = Column(Integer, primary_key=True)
    sezione = Column(String)
    studente_id = Column(Integer, ForeignKey('studenti.id'))
    studente = relationship("Studenti", back_populates="classi")

    def __repr__(self):
        return "<Classi(sezione='%s', studente_id='%s')>" % (self.sezione, self.studente_id)
    
engine = create_engine('sqlite:///database3.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Classi).delete()
session.commit()

session.query(Esami).delete()
session.commit()

session.query(Studenti).delete()
session.commit()


# Insert data
studenti = [
    {'nome': 'Mario', 'cognome': 'Rossi'},
    {'nome': 'Giuseppe', 'cognome': 'Verdi'},
    {'nome': 'Luca', 'cognome': 'Bianchi'},
    {'nome': 'Giorgia', 'cognome': 'Gialli'},
]

esami = [
    {'studente_id': 1, 'materia': 'Italiano', 'voto': 18},
    {'studente_id': 1, 'materia': 'Matematica', 'voto': 17},
    {'studente_id': 2, 'materia': 'Italiano', 'voto': 16},
    {'studente_id': 2, 'materia': 'Matematica', 'voto': 15},
    {'studente_id': 3, 'materia': 'Italiano', 'voto': 20},
    {'studente_id': 3, 'materia': 'Matematica', 'voto': 19},
    {'studente_id': 4, 'materia': 'Italiano', 'voto': 18},
    {'studente_id': 4, 'materia': 'Matematica', 'voto': 17},
]

classi = [
    {'sezione': '3A', 'studente_id': 1},
    {'sezione': '3B', 'studente_id': 2},
    {'sezione': '3C', 'studente_id': 3},
    {'sezione': '3D', 'studente_id': 4},
]

for studente in studenti:
    print(studente)
    session.add(Studenti(**studente))
    
for esame in esami:
    print(esame)
    session.add(Esami(**esame))
    
for classe in classi:
    print(classe)
    session.add(Classi(**classe))
    
session.commit()

rows = session.query(Studenti).join(Esami).filter(and_(Esami.voto >= 18, Esami.materia == 'Italiano')).filter(Esami.voto > 18)
for row in rows:
    print(row)

session.close()