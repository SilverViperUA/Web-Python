from flask import Flask, request, render_template, redirect, url_for, Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


class SportsEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()

sports_events_bp = Blueprint('sports_events', __name__)
api_sports_events = Api(sports_events_bp)


class SportsEventResource(Resource):
    def get(self, sports_event_id):
        sports_event = SportsEvent.query.get_or_404(sports_event_id)
        return {'id': sports_event.id, 'name': sports_event.name, 'year': sports_event.year, 'country': sports_event.country}

    def put(self, sports_event_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        parser.add_argument('year', type=int, required=True, help='Year cannot be blank')
        parser.add_argument('country', type=str, required=True, help='Country cannot be blank')

        args = parser.parse_args()
        sports_event = SportsEvent.query.get_or_404(sports_event_id)
        sports_event.name = args['name']
        sports_event.year = args['year']
        sports_event.country = args['country']
        db.session.commit()
        return {'message': 'Sports event updated successfully'}

    def delete(self, sports_event_id):
        sports_event = SportsEvent.query.get_or_404(sports_event_id)
        db.session.delete(sports_event)
        db.session.commit()
        return {'message': 'Sports event deleted successfully'}


class SportsEventsResource(Resource):
    def get(self):
        sports_events = SportsEvent.query.all()
        sports_events_data = [{'id': sports_event.id, 'name': sports_event.name, 'year': sports_event.year, 'country': sports_event.country} for sports_event in sports_events]
        return jsonify(sports_events_data)

    def post(self):
        try:
            if request.content_type == 'application/json':
                data = request.get_json()
            else:
                data = request.form
            if 'name' not in data or 'year' not in data or 'country' not in data:
                return {'message': 'Missing required data'}, 400
            new_sports_event = SportsEvent(name=data['name'], year=data['year'], country=data['country'])
            db.session.add(new_sports_event)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return {'message': str(e)}, 500


api_sports_events.add_resource(SportsEventResource, '/sports_event/<int:sports_event_id>')
api_sports_events.add_resource(SportsEventsResource, '/sports_events', endpoint='sports_events')


@sports_events_bp.route('/')
def get_sports_events():
    sports_events = SportsEvent.query.all()
    return render_template('index.html', sports_events=sports_events)


@sports_events_bp.route('/delete/<int:sports_event_id>', methods=['GET'])
def delete_sports_event(sports_event_id):
    sports_event = SportsEvent.query.get_or_404(sports_event_id)
    db.session.delete(sports_event)
    db.session.commit()
    return redirect(url_for('sports_events.get_sports_events'))


@sports_events_bp.route('/update/<int:sports_event_id>', methods=['GET', 'POST'])
def update_sports_event(sports_event_id):
    sports_event = SportsEvent.query.get_or_404(sports_event_id)

    if request.method == 'POST':
        sports_event.name = request.form['name']
        sports_event.year = request.form['year']
        sports_event.country = request.form['country']
        db.session.commit()
        return redirect(url_for('sports_events.get_sports_events'))

    return render_template('edit_sports_event.html', sports_event=sports_event)


app.register_blueprint(sports_events_bp)

if __name__ == '__main__':
    app.run(debug=True)
