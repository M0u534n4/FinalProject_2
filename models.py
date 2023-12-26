from ext import db
from flask_login import LoginManager, UserMixin
login_manager = LoginManager()

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.add(self)
        db.session.commit()


    def save(self):
        db.session.commit()

    


class User(db.Model, BaseModel, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

