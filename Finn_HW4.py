from flask import Flask
from flask import render_template, redirect, request, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import pymysql
#import secrets
import os

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASS')
dbhost = os.environ.get('DBHOST')
dbname = os.environ.get('DBNAME')

#conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class movie_names(db.Model):
    #__tablename__ = 'results'
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(255))


    def __repr__(self):
        return "id: {0} | movie name: {1}".format(self.movie_id, self.movie_name)

class MovieForm(FlaskForm):
    movie_name = StringField('Movie Name:', validators=[DataRequired()])


@app.route('/')
def index():
    all_movies = movie_names.query.all()
    return render_template('index.html', movies=all_movies, pageTitle='Movie Names')


@app.route('/movie/new', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        friend = movie_names(movie_name=form.movie_name.data)
        db.session.add(movie)
        db.session.commit()
        return redirect('/')

    return render_template('add_movie.html', form=form, pageTitle='Add A New Movie',
                            legend="Add A New Movie")



@app.route('/movie/<int:movie_id>', methods=['GET','POST'])
def friend(movie_id):
    movie = movie_names.query.get_or_404(movie_id)
    return render_template('movie.html', form=movie, pageTitle='Movie Details')



@app.route('/movie/<int:movie_id>/delete', methods=['POST'])
def delete_movie(movie_id):
    if request.method == 'POST':
        movie = movie_names.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        flash('Movie was successfully deleted')
        return redirect("/")
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
