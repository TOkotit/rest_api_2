from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader_id = IntegerField('id руководителя', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Кто работает', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')
