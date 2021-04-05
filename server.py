import os
import pymorphy2
# from data import db_session
# from data.comment import Comment

from currency_converter import CurrencyConverter, RateNotFoundError
from flask import Flask, render_template, redirect
from data.form import MainForm, Commenting

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myapp_secret_key'
converter = CurrencyConverter()
morph = pymorphy2.MorphAnalyzer()


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/converting", methods=['GET', 'POST'])
def converting():
    # Данные с форм
    form = MainForm()
    form2 = Commenting()
    # comment = Comment()
    # db_sess = db_session.create_session()

    number = form.data_in.data
    curr = form.select.data
    curr_2 = form.select2.data
    curr_short = curr[:3]
    curr2_short = curr_2[:3]

    # Первоначальное отсутствие данных - заглушка
    if number is None:
        number = '0'
        curr = form.select.default
        curr_2 = form.select2.default
    # if form2.comment.data is not None:
    #     comment.comment = form2.comment.data
    #     db_sess.add(comment)
    #     db_sess.commit()

    # Конвертация на основе данных с форм
    try:
        res = converter.convert(int(number), curr_short, curr2_short)
        res = str(round(res, 2)) + ' ' + curr2_short
    except ValueError:
        res = 'Ошибка ввода данных'
    except RateNotFoundError:
        res = 'Котировка валюты не найдена'

    # Конвертация одной единицы валюты
    try:
        res_2 = str(round(converter.convert(1, curr_short, curr2_short), 2))
    except RateNotFoundError:
        res_2 = 'Котировка не найдена'
    # Рендеринг шаблона
    return render_template('converting.html', form=form, form2=form2,
                           result=res,
                           result_2=f'1 {curr_short} равен {res_2} '
                                    f'{curr2_short}',
                           h_title=f'{curr[6:]} в {curr_2[6:]}')


@app.route("/add_comment", methods=['GET', 'POST'])
def adding():
    return 'Здесь пока ничего нет'


# TESTING
# if __name__ == '__main__':
#     # db_session.global_init("db/comments.db")
#     port = int(os.environ.get("PORT", 5000))
#     app.run(port=port, debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
