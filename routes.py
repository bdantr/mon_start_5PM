from flask import render_template
from app import app  # импортирую главный модуль сайта


@app.route('/')  #  если перейти на главную страницу сайта
def main():  # вызовется функция
    return render_template('index.html')  # вернуть шаблон index.html

@app.routs('/contacts')
def contacts():
    return render_template ('contacts.html')


@app.routs('/about')
def contacts():
    return render_template('about')
