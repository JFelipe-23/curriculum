from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_login import LoginManager, current_user, login_user, logout_user
import pprint as pp
from models import *
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba2e18ce248bab7ce9425333f0420b57a5f07dfef342e1876d3013a524acf416f813af3071a65e3860475fe8e81c3a42c3c8fa65051de39aa2037fa695b305a7bc7044a415eb'

# Configuración de LoginManager
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	for user in users:
		if str(user.id) == str(user_id):
			return user
	return None

# Ruta principal: mostrar todas las hojas de vida
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', cvs=cvs)

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if form.validate_on_submit():
		user = get_user(form.email.data)
		if user and user.check_password(form.password.data):
			login_user(user, remember=form.remember_me.data)
			return redirect(url_for('index'))
		else:
			return render_template('login_form.html', form=form, error='Credenciales incorrectas')
	return render_template('login_form.html', form=form)

# Ruta de cierre de sesión
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

# Ruta de registro
@app.route('/signup', methods=['GET', 'POST'])
def show_signup_form():
	form = SignupForm()
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if form.validate_on_submit():
		if get_user(form.email.data):
			return render_template('admin/signup_form.html', form=form, error='El correo ya está registrado')
		new_user = User(id=len(users)+1, name=form.name.data, email=form.email.data, password=form.password.data)
		users.append(new_user)
		login_user(new_user)
		return redirect(url_for('index'))
	return render_template('admin/signup_form.html', form=form)

# Ruta para ver un CV
@app.route('/cv/<int:cv_id>')
def view_cv(cv_id):
	cv = get_cv_by_id(cv_id)
	if not cv:
		return 'CV no encontrado', 404
	return render_template('cv_view.html', cv=cv)

# Ruta para crear un CV
@app.route('/cv/create', methods=['GET', 'POST'])
def create_cv():
	form = CVForm()
	if not current_user.is_authenticated:
		return redirect(url_for('login'))
	user_cvs = get_cv_by_user_id(current_user.id)
	if user_cvs:
		return redirect(url_for('edit_cv'))
	if form.validate_on_submit():
		new_cv = CV(
			id=len(cvs)+1,
			user_id=current_user.id,
			full_name=form.full_name.data,
			title=form.title.data,
			about_me=form.about_me.data,
			experience=[{
				'company': exp.company.data,
				'position': exp.position.data,
				'start_date': exp.start_date.data,
				'end_date': exp.end_date.data
			} for exp in form.experience],
			education=[{
				'school': edu.school.data,
				'degree': edu.degree.data,
				'start_date': edu.start_date.data,
				'end_date': edu.end_date.data
			} for edu in form.education],
			skills=[{
				'nombre': skill.nombre.data,
				'level': skill.level.data
			} for skill in form.skills]
		)
		cvs.append(new_cv)
		return redirect(url_for('view_cv', cv_id=new_cv.id))
	return render_template('admin/cv_form.html', form=form, is_new=True)

# Ruta para editar un CV
@app.route('/cv/edit', methods=['GET', 'POST'])
def edit_cv():
	if not current_user.is_authenticated:
		return redirect(url_for('login'))
	user_cvs = get_cv_by_user_id(current_user.id)
	if not user_cvs:
		return redirect(url_for('create_cv'))
	cv_data = user_cvs[0]
	form = CVForm()
	if request.method == 'GET':
		form = CVForm(data=cv_data)
	if form.validate_on_submit():
		for cv in cvs:
			if cv.user_id == current_user.id:
				cv.full_name = form.full_name.data
				cv.title = form.title.data
				cv.about_me = form.about_me.data
				cv.experience = [{
					'company': exp.company.data,
					'position': exp.position.data,
					'start_date': exp.start_date.data,
					'end_date': exp.end_date.data
				} for exp in form.experience]
				cv.education = [{
					'school': edu.school.data,
					'degree': edu.degree.data,
					'start_date': edu.start_date.data,
					'end_date': edu.end_date.data
				} for edu in form.education]
				cv.skills = [{
					'nombre': skill.nombre.data,
					'level': skill.level.data
				} for skill in form.skills]
				break
		return redirect(url_for('view_cv', cv_id=cv_data['id']))
	return render_template('admin/cv_form.html', form=form, is_new=False)

# API REST: Listar todos los CVs
@app.route('/api/cvs', methods=['GET'])
def api_get_cvs():
	return jsonify([cv.to_dict() for cv in cvs])

# API REST: Obtener un CV específico
@app.route('/api/cvs/<int:cv_id>', methods=['GET'])
def api_get_cv(cv_id):
	cv = get_cv_by_id(cv_id)
	if not cv:
		return jsonify({'error': 'CV no encontrado'}), 404
	return jsonify(cv)

if __name__ == '__main__':
    app.run(debug=True)
