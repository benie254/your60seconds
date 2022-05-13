from flask import render_template,redirect,url_for,request,abort
from . import main
from ..models import Pitch,Users,Comment
from flask_login import login_required,current_user
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos


# views
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    :return: index page + data
    """

    pitches = Pitch.query.all()
    comment_form = CommentForm()
    comments = Comment.query.all()

    love = Pitch.query.filter_by(pitch_category='love').all()
    entertainment = Pitch.query.filter_by(pitch_category='entertainment').all()
    sales = Pitch.query.filter_by(pitch_category='sales').all()
    job = Pitch.query.filter_by(pitch_category='job').all()
    uncategorized = Pitch.query.filter_by(pitch_category='uncategorized').all()

    if comment_form.validate_on_submit():
        comment_message = comment_form.message.data
        message = Comment(comment_message=comment_message)
        db.session.add(message)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('index.html', pitches=pitches, comment_form=comment_form, comments=comments, love=love,
                           sales=sales, entertainment=entertainment, job=job, uncategorized=uncategorized)


@main.route('/user/<uname>')
def profile(uname):

    user = Users.query.filter_by(username=uname).first()
    user_id = current_user._get_current_object().id
    user_pitches = Pitch.query.filter_by(user_id=user_id).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user,user_pitches=user_pitches)