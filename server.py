from currency_converter import CurrencyConverter
from flask import Flask, render_template, request, redirect
from form import MainForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
converter = CurrencyConverter()


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/converting", methods=['GET', 'POST'])
def converting():
    form = MainForm()
    number = form.data_in.data
    currency = form.select.data
    currency_2 = form.select2.data
    result_2 = str(round(converter.convert(1, currency, currency_2), 2))
    if number is None:
        number = '0'
    try:
        result = converter.convert(int(number), currency, currency_2)
        result = str(round(result, 2)) + ' ' + currency_2
    except ValueError:
        result = 'Ошибка ввода данных'
    return render_template('converting.html', form=form, result=result,
                           result_2=result_2, value=currency,
                           value_2=currency_2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')