from flask import Flask, jsonify, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_admin import Admin
from flasgger import Swagger
from config import Config
from models import User, Favourites, Characters, Planets, Starships
from utils import APIException, generate_sitemap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)

admin = Admin(app, name='Star Wars API', template_mode='bootstrap3')

swagger = Swagger(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.close()

@app.route('/')
def index():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = db.session.query(User).all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.query(User).get(user_id)
    if user is None:
        raise APIException('User not found', 404)
    return jsonify(user.serialize())

@app.route('/favourites', methods=['GET'])
def get_favourites():
    favourites = db.session.query(Favourites).all()
    return jsonify([favourite.serialize() for favourite in favourites])

@app.route('/favourites/<int:favourite_id>', methods=['GET'])
def get_favourite(favourite_id):
    favourite = db.session.query(Favourites).get(favourite_id)
    if favourite is None:
        raise APIException('Favourite not found', 404)
    return jsonify(favourite.serialize())

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = db.session.query(Characters).all()
    return jsonify([character.serialize() for character in characters])

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = db.session.query(Characters).get(character_id)
    if character is None:
        raise APIException('Character not found', 404)
    return jsonify(character.serialize())

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = db.session.query(Planets).all()
    return jsonify([planet.serialize() for planet in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = db.session.query(Planets).get(planet_id)
    if planet is None:
        raise APIException('Planet not found', 404)
    return jsonify(planet.serialize())

@app.route('/starships', methods=['GET'])
def get_starships():
    starships = db.session.query(Starships).all()
    return jsonify([starship.serialize() for starship in starships])

@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):
    starship = db.session.query(Starships).get(starship_id)
    if starship is None:
        raise APIException('Starship not found', 404)
    return jsonify(starship.serialize())

@app.errorhandler(APIException)
def handle_api_exception(error):
    return jsonify(error.to_dict()), error.status_code

if __name__ == '__main__':
    app.run(debug=True)