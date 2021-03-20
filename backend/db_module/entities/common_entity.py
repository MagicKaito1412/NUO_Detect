from backend.db_module.app import db
from sqlalchemy.dialects.postgresql import *

DB_USER = 'u1'


class CoreEntity(db.Model):
    __abstract__ = True

    created_by = db.Column(name='created_by', type_=VARCHAR(150), nullable=False)
    created_date = db.Column(name='created_date', type_=TIMESTAMP, nullable=False, default=db.func.now())
    update_by = db.Column(name='update_by', type_=VARCHAR(150))
    update_date = db.Column(name='update_date', type_=TIMESTAMP)
    version = db.Column(name='version', type_=BIGINT, nullable=False, default=0)

    def setSpecialField(self, created_by=None, create_date=None, update_by=None, update_date=None):
        if created_by is not None:
            self.created_by = created_by
        if create_date is not None:
            self.created_date = create_date
        if update_by is not None:
            self.update_by = update_by
        if update_date is not None:
            self.update_date = update_date

    def create(self, created_by=DB_USER, create_date=db.func.now()):
        self.setSpecialField(created_by=created_by, create_date=create_date)
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, update_by=DB_USER, update_date=db.func.now()):
        self.setSpecialField(update_by=update_by, update_date=update_date)
        self.version = self.version + 1
        db.session.commit()
        return self

    def save(self, save_by=DB_USER):
        if self.id is None:
            return self.create(created_by=save_by)
        else:
            return self.update(update_by=save_by)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self
