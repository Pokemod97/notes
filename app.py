from flask import *
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('index.html', notes=session['notes'])


@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        if session.get('notes') is None:
            session['notes'] = []
        session['notes'].append((request.form['title'], request.form['note']))
        session.modified = True
        return redirect(url_for('index'))
    return render_template('post.html')


if __name__ == '__main__':
    app.run()
