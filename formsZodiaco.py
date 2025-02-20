from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField
from wtforms import validators, EmailField


class FormZodiaco(Form):
    nombre = StringField('Nombre', [
    validators.DataRequired(message='El campo es requerido'),
    validators.Regexp(r'^[^0-9]*$', message='No se permiten números')  
    ])

    apellido_paterno = StringField('Apellido Paterno', [
    validators.DataRequired(message='El campo es requerido'),
    validators.Regexp(r'^[^0-9]*$', message='No se permiten números') 
    ])

    apellido_materno = StringField('Apellido Materno', [
    validators.DataRequired(message='El campo es requerido'),
    validators.Regexp(r'^[^0-9]*$', message='No se permiten números')  
    ])

    dia = IntegerField('Día', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=31, message='El día debe estar entre 1 y 31')
    ])

    mes = IntegerField('Mes', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=12, message='El mes debe estar entre 1 y 12')
    ])

    anio = IntegerField('Año', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1900, max=2025, message='El año debe ser válido')
    ])
    
    sexo = RadioField('Sexo', choices=[
        ('M', 'Masculino'),('F', 'Femenino')
    ], validators=[validators.DataRequired(message='El campo es requerido')])
    
    submit = SubmitField('Calcular Signo')