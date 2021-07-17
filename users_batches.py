from ..models import db

users_batches = db.Table('users_batches',
    db.Column('batch_fk', db.Integer, db.ForeignKey('batchs.id')),
    db.Column('user_fk', db.Integer, db.ForeignKey('users.id'))
)