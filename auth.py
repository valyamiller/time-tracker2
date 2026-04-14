from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from werkzeug.security import check_password_hash

def init_auth_routes(app):
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password) and user.is_active:
                login_user(user)
                flash('Успешный вход в систему!', 'success')
                if user.is_admin():
                    return redirect(url_for('admin'))
                return redirect(url_for('dashboard'))
            else:
                flash('Неверное имя пользователя или пароль', 'error')
        
        return render_template('login.html')
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Вы вышли из системы', 'info')
        return redirect(url_for('login'))
    
    @app.route('/change_password', methods=['POST'])
    @login_required
    def change_password():
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        
        if current_user.check_password(old_password):
            current_user.set_password(new_password)
            db.session.commit()
            flash('Пароль успешно изменен!', 'success')
        else:
            flash('Неверный текущий пароль', 'error')
        
        return redirect(url_for('profile'))