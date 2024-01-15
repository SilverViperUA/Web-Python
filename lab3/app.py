from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

# Функція для отримання інформації про операційну систему
def get_os_info():
    return os.name

# Функція для отримання інформації user_agent
def get_user_agent():
    return request.user_agent.string if request else "Not available"

# Функція для отримання поточного часу
def get_current_time():
    return datetime.now()

# Додаємо фільтр для форматування дати
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

# Список навичок
my_skills = ["Python", "Flask", "HTML", "CSS", "JavaScript", "SQL", "Git"]

@app.route('/')
def index():
    os_info = get_os_info()
    user_agent = get_user_agent()
    current_time = get_current_time()

    return render_template('base.html', os_info=os_info, user_agent=user_agent, current_time=current_time, my_skills=my_skills)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/skills/<int:id>')
def skills(id):
    if id is not None and 0 <= id < len(my_skills):
        # Відобразити навичку зі списку за відповідним id
        skill = my_skills[id]
        return f"Навичка з id {id}: {skill}"
    else:
        # Відобразити всі навички та їх загальну кількість
        skills_list = ', '.join(my_skills)
        return f"Всі навички: {skills_list}. Загальна кількість: {len(my_skills)}"

if __name__ == '__main__':
    app.run(debug=True)
