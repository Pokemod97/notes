from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
db.session.echo = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
from models import Note

db.create_all()
db.session.commit()


@app.route('/')
def index():
    return render_template('index.html', notes=Note.query.all())


@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        note = Note(title=request.form['title'], body=request.form['note'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html')


if __name__ == '__main__':
    app.run()
