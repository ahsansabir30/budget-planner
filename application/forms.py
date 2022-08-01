from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired

class PlanCreationForm(FlaskForm):
    name = StringField('Plan Name', validators=[
        DataRequired()
    ])
    budget = DecimalField('Budget', places=2, validators=[
        DataRequired()
    ])
    submit = SubmitField('Submit')

class ExpenseForm(FlaskForm):
    type = StringField('Expense Type', validators=[
        DataRequired()
    ])
    expense = DecimalField('Expense', places=2, validators=[
        DataRequired()
    ])
    submit = SubmitField('Save')
