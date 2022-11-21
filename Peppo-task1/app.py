from flask import Flask
from flask_restful import Api
from db import db
from resources.resource import Person, MultiplePerson, PersonDetails

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://snegha:5negha#T1b1l420@localhost/Flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()
api = Api(app)

api.add_resource(Person, "/person/<string:PersonId>")
api.add_resource(PersonDetails, "/person")

api.add_resource(MultiplePerson, "/multiple/")


if __name__ == '__main__':
    app.run(debug=True)
