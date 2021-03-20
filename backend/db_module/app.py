import sys
import os
sys.path.append(os.path.sep.join(sys.path[0].split(sep=os.path.sep)[:-2]))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from backend.db_module.entities import entities

app = Flask(__name__,)
app.url_map.strict_slashes = False

with app.app_context():
    db = SQLAlchemy(app)


def main():
    migrate = Migrate(app, db)
    app.config['SECRET_KEY'] = 'a really really really really long secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u1:1@127.0.0.1:5432/nuo_detect?client_encoding=utf8'
    manager = Manager(app)
    manager.add_command('runserver', Server(host='127.0.0.1', port=5040))
    manager.add_command('db', MigrateCommand)

    @manager.command
    def drop():
        entities.User.query.delete()
        entities.Doctor.query.delete()
        entities.Patient.query.delete()
        entities.EKG.query.delete()

        db.session.commit()

    manager.run()


if __name__ == '__main__':
    main()
