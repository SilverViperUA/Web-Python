from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registration_form():
    first_name = None
    last_name = None
    country = None

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        country = request.form.get('country')

    return render_template('form.html', first_name=first_name, last_name=last_name, country=country)

if __name__ == '__main__':
    app.run(debug=True)
