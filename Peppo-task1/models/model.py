from db import db


class PersonModel(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True)
    PersonName = db.Column(db.String(100))
    PersonAge = db.Column(db.Integer)
    PersonAddress = db.Column(db.String(100))

    def __init__(self, PersonName, PersonAge, PersonAddress):
        self.PersonName = PersonName
        self.PersonAge = PersonAge
        self.PersonAddress = PersonAddress

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_in_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
