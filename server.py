import os
import pymorphy2

from currency_converter import CurrencyConverter, RateNotFoundError
from flask import Flask, render_template, redirect

from data import db_session
from data.comment import Comment
from data.form import MainForm, Commenting

# Конфигурация приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp_secret_key'
# API ключи капчи
app.config['RECAPTCHA_PUBLIC_KEY'] = \
    '6Lfec60aAAAAAIVvWcgR77i_ziytfdj32T7iyJ8H'
app.config['RECAPTCHA_PRIVATE_KEY'] = \
    '6Lfec60aAAAAAD566qZCnsBPj_f2ZmS5WsWTL5NH '
# Сторонние библиотеки
converter = CurrencyConverter()
morph = pymorphy2.MorphAnalyzer()


# Обработчик главной страницы
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Обработчик страницы конвертации
@app.route("/converting", methods=['GET', 'POST'])
def converting():
    # Инициализация форм
    currency_form = MainForm()
    commenting_form = Commenting()
    # Создание сессии базы данных
    db_sess = db_session.create_session()

    # Сбор данных с формы
    # Число - денежная величина
    value = currency_form.data_in.data
    # Исходная валюта
    curr_in = currency_form.select.data
    # В какую валюту конвертировать
    curr_out = currency_form.select2.data

    # Короткие символы валют
    curr_in_short = curr_in[:3]
    curr_out_short = curr_out[:3]

    # Первоначальное отсутствие данных
    if value is None:
        value = '0'
        curr_in = currency_form.select.default
        curr_out = currency_form.select2.default

    try:
        result = converter.convert(int(value), curr_in_short, curr_out_short)
        result = str(round(result, 2)) + ' ' + curr_out_short
    except ValueError:
        result = 'Ошибка ввода данных'
    except RateNotFoundError:
        result = 'Котировка валюты не найдена'

    # Конвертация одной единицы валюты
    try:
        result_ones = converter.convert(1, curr_in_short, curr_out_short)
        result_ones = str(round(result_ones, 2))
    except RateNotFoundError:
        result_ones = 'Котировка не найдена'

    return render_template(
        'converting.html',
        currency_form=currency_form,
        commenting_form=commenting_form,
        result=result,
        result_ones=f'1 {curr_in_short} равен {result_ones} {curr_out_short}',
        h_title=f'{curr_in[6:]} в {curr_out[6:]}',
        comments=reversed(db_sess.query(Comment).all())
    )


# Добавление комментария в БД
@app.route("/add_comment", methods=['GET', 'POST'])
def adding():
    commenting_form = Commenting()
    comment_db = Comment()
    db_sess = db_session.create_session()
    comment_db.text = commenting_form.comment.data
    comment_db.email = commenting_form.email.data
    comment_db.username = commenting_form.username.data
    db_sess.add(comment_db)
    db_sess.commit()
    return redirect('/converting')


# TESTING
# if __name__ == '__main__':
#     db_session.global_init("db/comments.db")
#     port = int(os.environ.get("PORT", 5000))
#     app.run(port=port, debug=True)

if __name__ == '__main__':
    db_session.global_init("db/comments.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
