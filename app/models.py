from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


class Users(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    pitch_upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    pitch_downvote = db.relationship('Downvote', backref='user', lazy='dynamic')
    pitch_comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Users {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Pitch(db.Model):
    """
    defines Pitch objects
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String(255))
    pitch_content = db.Column(db.String(255))
    pitch_category = db.Column(db.String(255), index=True, nullable=False)
    pitch_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_upvote = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    pitch_downvote = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    pitch_comment = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches