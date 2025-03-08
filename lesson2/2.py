from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pluto_is_planet_and_cuba_is_free'

@app.route('/')
@app.route('/index/<username>')
def news(username):
    return render_template('index.html', title=username)

@app.route('/index/<username>')
def news(username):
    return render_template('index.html', title=username)


@app.route('/training/<username>')
def image(username):
    return render_template('training.html', title=username)

@app.route('/list_prof/<t>')
def profs(t):
    return render_template('professions.html', t=t)

@app.route('/answer')
@app.route('/auto_answer')
def answer(params):
    return render_template('professions.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')