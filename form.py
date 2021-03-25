from currency_converter import CurrencyConverter
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

converter = CurrencyConverter()
cur_list = sorted(list(converter.currencies))


class MainForm(FlaskForm):
    select = SelectField(choices=cur_list,
                         default=cur_list[cur_list.index('USD')])
    select2 = SelectField(choices=cur_list,
                          default=cur_list[cur_list.index('RUB')])
    data_in = StringField('Введите сюда', validators=[DataRequired()])
    submit = SubmitField('>>>')
