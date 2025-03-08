from flask import Flask, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pluto_is_planet_and_cuba_is_free'


@app.route('/')
def page():
    return "Отбор астронавтов"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def image_mars():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <p, class="fs-1", style="color: red">Жди нас, Марс!</p>
                            <br/>
                            <img src="{url_for('static', filename='img/mars.png')}"></img>
                            <br>
                            <div class="alert alert-dark", role="alert">Человечество вырастит из детства.</div>
                            <div class="alert alert-success", role="alert">Человечеству мала одна планета.</div>
                            <div class="alert alert-secondary", role="alert">Мы сделаем обитаемыми безжизненные планеты.</div>
                            <div class="alert alert-warning", role="alert">И начнём с Марса!</div>
                            <div class="alert alert-danger", role="alert">Присоединяйся!</div>
                          <body>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">                                    
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер!</option>
                                        </select>
                                     </div>
                                    <label for="eduSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof1">

                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof2">

                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof3">

                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof4">

                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof5">

                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof6">

                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>


                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марск?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname', ""))
        print(request.form.get('name', ""))
        print(request.form.get('email', ""))
        print(request.form.get('edu', ""))
        print(request.form.get('about', ""))
        print(request.form.get('accept', ""))
        print(request.form.get('sex', ""))
        print("Инженер-исследователь -", request.form.get('prof', "off"))
        print("Инженер-строитель -", request.form.get('prof1', "off"))
        print("Пилот -", request.form.get('prof2', "off"))
        print("Метеоролог -", request.form.get('prof3', "off"))
        print("Инженер по жизнеобеспечению -", request.form.get('prof4', "off"))
        print("Инженер по радиационной защите -", request.form.get('prof5', "off"))
        print("Врач -", request.form.get('prof6', "off"))
        print("Экзобиолог -", request.form.get('prof7', "off"))
        print(request.form.get('file', ""))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
