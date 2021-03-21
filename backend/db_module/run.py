import sys
import os
sys.path.append(os.path.sep.join(sys.path[0].split(sep=os.path.sep)[:-2]))

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand

from backend.db_module import app
from backend.db_module.entities import entities


with app.app_context():
    db = SQLAlchemy(app)


def _make_context():
    return dict(app=app, db=db, models=entities)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)


@manager.command
def drop():
    entities.User.query.delete()
    entities.Doctor.query.delete()
    entities.Patient.query.delete()
    entities.EKG.query.delete()

    db.session.commit()


if __name__ == '__main__':
    manager.run()
