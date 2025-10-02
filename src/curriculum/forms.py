from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, IntegerField, FieldList, FormField, Form
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange



# Formulario de registro
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

# Formulario de inicio de sesión
class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesión')

# Formulario de experiencia laboral
class ExperienceForm(Form):
    company = StringField('Empresa', validators=[DataRequired()])
    position = StringField('Cargo', validators=[DataRequired()])
    start_date = DateField('Fecha de inicio', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('Fecha de finalización', validators=[Optional()], format='%Y-%m-%d')
    submit = SubmitField('Guardar experiencia')

# Formulario de formación académica
class EducationForm(Form):
    school = StringField('Institución', validators=[DataRequired()])
    degree = StringField('Título', validators=[DataRequired()])
    start_date = DateField('Fecha de inicio', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('Fecha de finalización', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Guardar formación')

# Formulario de habilidad
class SkillForm(Form):
    nombre = StringField('Habilidad', validators=[DataRequired()])
    level = IntegerField('Nivel (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])

# Formulario principal de CV
class CVForm(FlaskForm):
    full_name = StringField('Nombre completo', validators=[DataRequired()])
    title = StringField('Título profesional', validators=[DataRequired()])
    about_me = TextAreaField('Sobre mí', validators=[Length(max=1000)])

    experience = FieldList(FormField(ExperienceForm), min_entries=1)
    education = FieldList(FormField(EducationForm), min_entries=1)
    skills = FieldList(FormField(SkillForm), min_entries=1)

    submit = SubmitField('Guardar CV')
