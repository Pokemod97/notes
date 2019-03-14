from flask import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form.get('title'))
    return 'hi'


if __name__ == '__main__':
    app.run()
