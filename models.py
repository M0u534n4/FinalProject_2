from ext import db, app
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
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
        new_user = User(username="admin_user", password="password", role="admin")
        new_user.create()


        
        normal_user = User(username="normal_user", password="password", role="guest")
        normal_user.create()
        



