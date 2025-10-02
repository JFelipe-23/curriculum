from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

users = []
cvs = []

class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.is_admin = is_admin
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"

def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None

class CV:
    def __init__(self, id, user_id, full_name, title, about_me, experience, education, skills):
        self.id = id
        self.user_id = user_id
        self.full_name = full_name
        self.title = title
        self.about_me = about_me
        self.experience = experience
        self.education = education
        self.skills = skills

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "title": self.title,
            "about_me": self.about_me,
            "experience": self.experience,
            "education": self.education,
            "skills": self.skills
        }

def get_cv_by_user_id(user_id):
    return [cv.to_dict() for cv in cvs if cv.user_id == user_id]

def get_cv_by_id(cv_id):
    for cv in cvs:
        if cv.id == cv_id:
            return cv.to_dict()
    return None